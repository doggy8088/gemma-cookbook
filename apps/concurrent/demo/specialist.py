"""
specialist.py — Specialist agent for the multi-agent demo.

Polls for a task file, calls the LLM, streams the response, writes the result.

Usage:
    python specialist.py --name french --emoji "🇫🇷" --color "1;34" \
        --api-url http://127.0.0.1:8080/v1/chat/completions
"""

import argparse
import json
import os
import time

from utils import COMMS_DIR, RESET, DIM, stream_llm

POLL_INTERVAL = 0.5


def wait_for_task(name: str) -> dict:
    """Poll for a task file."""
    task_path = os.path.join(COMMS_DIR, f"task_{name}.json")
    while True:
        if os.path.exists(task_path):
            time.sleep(0.1)
            try:
                with open(task_path, "r") as f:
                    task = json.load(f)
                os.remove(task_path)
                return task
            except (json.JSONDecodeError, IOError):
                pass
        time.sleep(POLL_INTERVAL)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--emoji", default="🤖")
    parser.add_argument("--color", default="1;37")
    parser.add_argument("--api-url", default="http://127.0.0.1:8080/v1/chat/completions")
    args = parser.parse_args()

    color = args.color
    name = args.name
    display = name.upper().replace("_", " ")

    # Header
    print(f"\033[{color}m{'━' * 45}{RESET}")
    print(f"\033[{color}m  {args.emoji}  {display}{RESET}")
    print(f"\033[{color}m{'━' * 45}{RESET}")
    print(f"{DIM}  Waiting for task...{RESET}\n")

    # Wait → Execute → Report
    task = wait_for_task(name)
    instruction = task.get("instruction", "")
    system_prompt = task.get("system_prompt", "")

    print(f"\033[{color}m📋 {instruction[:60]}...{RESET}\n")
    print(f"\033[{color}m{'─' * 45}{RESET}\n")

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": instruction})

    result = stream_llm(args.api_url, messages, agent_name=name, color=color)

    # Write result
    result_path = os.path.join(COMMS_DIR, f"result_{name}.json")
    with open(result_path, "w") as f:
        json.dump({"task_id": task.get("task_id", ""), "result": result}, f)

    print(f"\n\n\033[{color}m{'─' * 45}{RESET}")
    print(f"\033[{color}m  ✅ {args.emoji}  {display} — Done!{RESET}")
    print(f"\033[{color}m{'─' * 45}{RESET}")

    input("\nPress Enter to close...")


if __name__ == "__main__":
    main()
