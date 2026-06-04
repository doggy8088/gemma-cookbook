https://github.com/user-attachments/assets/00b78c38-597b-4a84-8a18-9c1644f94669
在本地 [`llama-server`](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) 上執行 **N 個並發 Gemma 4 個實例** 並可視化它們實時工作。
這些 Gemma 4 實例可以在多種場景中執行，例如生成 SVG、翻譯文本、生成代碼和生成 ASCII 藝術作品。
## 先決條件

- **macOS** (uses AppleScript for Terminal window management)
- **[uv](https://github.com/astral-sh/uv)** for package management
- **來自 [llama.cpp](https://github.com/ggml-org/llama.cpp) 的 llama-server** 在 `localhost:8080` 上執行

## 快速入門

**1.安裝依賴項**
```bash
uv sync
```

**2.啟動 llama-server**
如果您安裝了 `llama.cpp` 和本地 [Gemma 4 GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF)，您可以使用以下命令啟動 `llama-server`：
```bash
llama-server -m gemma-4-26B-A4B-it-UD-Q4_K_M.gguf -c 70000 -np 10 --metrics --reasoning off
```

> [！提示]
> 將 `-np` 設定為並發 Gemma 4 個實例的數量 + 1（對於協調器）。
> 每個實例都有自己的插槽。每個槽的上下文 = `-c` / `-np`。

**3.執行演示**
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

這將在網格中開啟 macOS 終端機視窗：頂部是儀表板、編排器和下面的 N Gemma 4 個實例。
## 新增場景

編輯`demo/scenarios.py`：
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

然後執行：
```bash
bash run.sh --scenario my_scenario --topic "My Topic"
```
