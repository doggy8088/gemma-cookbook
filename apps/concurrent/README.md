https://github.com/user-attachments/assets/00b78c38-597b-4a84-8a18-9c1644f94669

Run **N concurrent Gemma 4 instances** on a local [`llama-server`](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) and visualize them working in real time. 

These Gemma 4 instances can be run across several scenarios, such as generating SVGs, translating text, generating code, and generating ASCII art.

## Prerequisites

- **macOS** (uses AppleScript for Terminal window management)
- **[uv](https://github.com/astral-sh/uv)** for package management
- **llama-server** from [llama.cpp](https://github.com/ggml-org/llama.cpp) running on `localhost:8080`

## Quick Start

**1. Install dependencies**

```bash
uv sync
```

**2. Start llama-server**

If you have `llama.cpp` installed and a local [Gemma 4 GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF), you can start `llama-server` with:

```bash
llama-server -m gemma-4-26B-A4B-it-UD-Q4_K_M.gguf -c 70000 -np 10 --metrics --reasoning off
```

> [!TIP]
> Set `-np` to the number of concurrent Gemma 4 instances + 1 (for the orchestrator).
> Each instance gets its own slot. Context per slot = `-c` / `-np`.

**3. Run a demo**

```bash
# Generate SVGs
bash run.sh --scenario svg --topic "Technology and AI" --tasks 10

# Translate text
bash run.sh --scenario translate --topic "Gemma 4 is a family of models released by Google DeepMind." --tasks 10

# Code Gallery
bash run.sh --scenario code --topic "FizzBuzz" --tasks 10

# ASCII Art
bash run.sh --scenario ascii --topic "animals" --tasks 10
```

This opens macOS Terminal windows in a grid: a dashboard on top, the orchestrator, and N Gemma 4 instances below.

## Adding a New Scenario

Edit `demo/scenarios.py`:

```python
def make_my_agents(n: int = 10) -> list[dict]:
    return [
        {
            "name": f"Agent {i+1}",
            "emoji": "🎯",
            "color": _COLORS[i % len(_COLORS)],
            "direct_instruction": "Process {topic} in style X",
        }
        for i in range(n)
    ]

MY_PLAN = {
    "system": 'Output a JSON array with {n_agents} objects, each with "name" and "instruction".',
    "user": 'Topic: "{topic}". Agents: {agent_list}.',
}

MY_SYSTEM = "You are a ... Output ONLY ..."

def my_template(topic, results, agents, tasks=None):
    # Build HTML from results dict
    ...

SCENARIOS["my_scenario"] = {
    "make_agents": make_my_agents,
    "plan": MY_PLAN,
    "template": my_template,
    "system_prompt": MY_SYSTEM,
    "default_n": 10,
}
```

Then run:

```bash
bash run.sh --scenario my_scenario --topic "My Topic"
```
