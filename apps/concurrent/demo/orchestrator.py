"""
orchestrator.py — Orchestrator for the multi-agent demo.

Uses the LLM to decompose a topic into per-agent tasks, dispatches them
via JSON files, collects results, and assembles a visual HTML page.

Usage:
    python orchestrator.py --scenario translate --topic "Gemma is an open AI model"
    python orchestrator.py --scenario svg_art --topic "Technology and AI"
"""

import argparse
import json
import os
import subprocess
import time

from scenarios import get_scenario
from utils import (
    COMMS_DIR, BUILD_DIR, RESET, DIM, BOLD, CYAN, GREEN, YELLOW, WHITE,
    stream_llm,
)

POLL_INTERVAL = 0.5


# ─── Step 1: Plan ───────────────────────────────────────────

def plan_tasks(api_url: str, scenario: dict, topic: str) -> list[dict]:
    """Use the LLM to generate specific instructions per agent."""
    agents = scenario["agents"]
    plan = scenario["plan"]

    print(f"\n{CYAN}{'━' * 60}{RESET}")
    print(f"{CYAN}  🧠 STEP 1: PLANNING{RESET}")
    print(f"{CYAN}{'━' * 60}{RESET}\n")

    agent_list = ", ".join(a["name"] for a in agents)
    user_prompt = plan["user"].replace("{topic}", topic).replace("{agent_list}", agent_list)

    print(f"{DIM}Generating agent instructions...{RESET}\n")
    plan_tokens = max(1024, len(agents) * 200)

    messages = [
        {"role": "system", "content": plan["system"]},
        {"role": "user", "content": user_prompt},
    ]
    raw = stream_llm(api_url, messages, agent_name="orchestrator",
                     color="1;36", max_tokens=plan_tokens)
    print("\n")

    # Extract JSON array (skip any reasoning preamble)
    start_idx = raw.find('[')
    end_idx = raw.rfind(']')

    if start_idx != -1 and end_idx != -1:
        json_str = raw[start_idx:end_idx + 1]
    else:
        json_str = raw

    try:
        tasks = json.loads(json_str)
        print(f"{GREEN}✅ Plan: {len(tasks)} tasks{RESET}\n")
        for t in tasks:
            name = t.get("name", "?")
            agent = next((a for a in agents if a["name"] == name), None)
            emoji = agent["emoji"] if agent else "❓"
            instr = t.get("instruction", "")[:50]
            print(f"  {emoji}  {BOLD}{name}{RESET} {DIM}{instr}...{RESET}")
        print()
        return tasks
    except json.JSONDecodeError:
        print(f"{YELLOW}⚠️  Parse failed — using fallback{RESET}\n")
        return [{"name": a["name"], "instruction": f"Work on: {topic}"} for a in agents]


# ─── Step 2: Dispatch ───────────────────────────────────────

def dispatch(tasks: list[dict], agents: list[dict], system_prompt: str = ""):
    """Write task files so specialist agents can pick them up."""
    print(f"{CYAN}{'━' * 60}{RESET}")
    print(f"{CYAN}  🚀 STEP 2: DISPATCHING{RESET}")
    print(f"{CYAN}{'━' * 60}{RESET}\n")

    task_id = f"task_{int(time.time())}"

    for task in tasks:
        name = task["name"]
        path = os.path.join(COMMS_DIR, f"task_{name}.json")
        with open(path, "w") as f:
            json.dump({
                "task_id": task_id,
                "instruction": task["instruction"],
                "system_prompt": system_prompt,
            }, f)

        agent = next((a for a in agents if a["name"] == name), None)
        emoji = agent["emoji"] if agent else "📦"
        print(f"  {emoji}  {name}")

    print(f"\n{GREEN}✅ {len(tasks)} tasks dispatched!{RESET}\n")


# ─── Step 3: Collect ────────────────────────────────────────

def collect(tasks: list[dict], agents: list[dict]) -> dict[str, str]:
    """Wait for all agents to write their result files."""
    print(f"{YELLOW}⏳ Waiting for agents...{RESET}\n")

    results = {}
    pending = {t["name"] for t in tasks}

    while pending:
        for name in list(pending):
            path = os.path.join(COMMS_DIR, f"result_{name}.json")
            if os.path.exists(path):
                time.sleep(0.1)
                try:
                    with open(path, "r") as f:
                        data = json.load(f)
                    os.remove(path)
                    results[name] = data.get("result", "")
                    pending.remove(name)
                    done = len(tasks) - len(pending)
                    print(f"  {GREEN}✅{RESET}  Agent {done}/{len(tasks)} done")
                except (json.JSONDecodeError, IOError):
                    pass
        if pending:
            time.sleep(POLL_INTERVAL)

    print(f"\n{GREEN}🎉 All agents finished!{RESET}\n")
    return results


# ─── Step 4: Assemble ───────────────────────────────────────

def assemble(scenario: dict, topic: str, results: dict, tasks: list = None):
    """Build the final HTML page from all agent results."""
    print(f"{CYAN}{'━' * 60}{RESET}")
    print(f"{CYAN}  🔧 STEP 3: ASSEMBLING{RESET}")
    print(f"{CYAN}{'━' * 60}{RESET}\n")

    from scenarios import build_page
    page_html = build_page(topic, scenario, results, tasks=tasks)

    os.makedirs(BUILD_DIR, exist_ok=True)
    path = os.path.join(BUILD_DIR, "index.html")
    with open(path, "w") as f:
        f.write(page_html)

    print(f"  {GREEN}✅ Assembled: index.html{RESET}")

    try:
        subprocess.run(["open", path], check=True)
        print(f"  {GREEN}🌍 Opened in browser!{RESET}")
    except Exception:
        pass

    return path


# ─── Main ────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="translate")
    parser.add_argument("--topic", default="Gemma is Google's most capable open AI model")
    parser.add_argument("--tasks", type=int, default=None,
                        help="Number of tasks/LLMs (default: scenario default)")
    parser.add_argument("--api-url", default="http://127.0.0.1:8080/v1/chat/completions")
    args = parser.parse_args()

    scenario = get_scenario(args.scenario, n_agents=args.tasks)
    agents = scenario["agents"]

    print(f"\n{CYAN}{'━' * 60}{RESET}")
    print(f"{CYAN}  🏗️  MULTI-AGENT ORCHESTRATOR{RESET}")
    print(f"{CYAN}{'━' * 60}{RESET}")
    print(f"\n{WHITE}  Scenario:{RESET} {args.scenario}")
    print(f"{WHITE}  Topic:{RESET} {args.topic}")
    print(f"{DIM}  {len(agents)} agents{RESET}\n")

    # Clean communication directories
    for d in [COMMS_DIR, BUILD_DIR]:
        if os.path.exists(d):
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))
        else:
            os.makedirs(d)

    tasks = plan_tasks(args.api_url, scenario, args.topic)
    dispatch(tasks, agents, system_prompt=scenario.get("system_prompt", ""))
    results = collect(tasks, agents)
    assemble(scenario, args.topic, results, tasks=tasks)

    print(f"\n{CYAN}{'━' * 60}{RESET}")
    print(f"{CYAN}  ✅ COMPLETE{RESET}")
    print(f"{CYAN}{'━' * 60}{RESET}\n")

    input("Press Enter to close...")


if __name__ == "__main__":
    main()
