"""
scenarios.py — Scenario definitions for the multi-agent demo.

Each scenario defines:
  - make_agents(n):   Returns a list of agent dicts
  - plan:             System + user prompts for orchestrator planning
  - system_prompt:    System prompt for specialist agents
  - render_card:      Function(agent, result) → inner HTML for one card
  - title:            Page title
  - default_n:        Default number of agents


─── Adding a New Scenario ──────────────────────────────────

1. Create a make_xxx_agents(n) function returning agent dicts
2. Define XXX_SYSTEM prompt for specialists
3. Define XXX_PLAN with "system" and "user" prompts
   (use {n_agents}, {topic}, {agent_list} placeholders)
4. Create xxx_card(agent, result) → inner HTML for one card
5. Register in SCENARIOS dict with title and render_card

Then run:  bash run.sh --scenario my_scenario --topic "My Topic"
"""

import html


# ─── Palettes ───────────────────────────────────────────────

_COLORS = [
    "1;35", "1;36", "1;33", "1;32", "1;34", "0;36", "0;35", "0;33", "0;32", "0;34",
    "1;31", "0;31", "1;37", "0;37", "1;35", "1;36", "1;33", "1;32", "1;34", "0;36",
]

_LANG_EMOJIS = [
    "🇫🇷", "🇪🇸", "🇩🇪", "🇯🇵", "🇨🇳", "🇰🇷", "🇸🇦", "🇮🇳", "🇧🇷", "🇷🇺",
    "🇮🇹", "🇹🇷", "🇻🇳", "🇹🇭", "🇳🇱", "🇵🇱", "🇸🇪", "🇬🇷", "🇮🇩", "🇺🇦",
]

_LANG_NAMES = [
    "french", "spanish", "german", "japanese", "chinese", "korean",
    "arabic", "hindi", "portuguese", "russian", "italian", "turkish",
    "vietnamese", "thai", "dutch", "polish", "swedish", "greek",
    "indonesian", "ukrainian",
]

_SVG_STYLES = [
    "minimalist", "cyberpunk", "watercolor", "pixel art",
    "abstract", "geometric", "neon", "vintage",
    "pop art", "isometric", "steampunk", "monochrome",
    "low poly", "surreal", "line art", "flat design",
    "3D render", "anime", "cubism", "synthwave",
]

_CODE_LANGS = [
    "python", "javascript", "rust", "go", "c", "java", "ruby", "swift",
    "kotlin", "typescript", "php", "scala", "haskell", "elixir",
    "lua", "perl", "r", "julia", "dart", "zig",
]

_CODE_EMOJIS = [
    "🐍", "📜", "🦀", "🐹", "⚙️", "☕", "💎", "🍎",
    "🟣", "🔷", "🐘", "🔴", "λ", "💧",
    "🌙", "🐪", "📊", "🔮", "🎯", "⚡",
]






# ─── Agent Factories ───────────────────────────────────────

def make_translate_agents(n: int = 10) -> list[dict]:
    return [
        {
            "name": _LANG_NAMES[i % len(_LANG_NAMES)],
            "emoji": _LANG_EMOJIS[i % len(_LANG_EMOJIS)],
            "color": _COLORS[i % len(_COLORS)],
            "direct_instruction": f"Translate this into {_LANG_NAMES[i % len(_LANG_NAMES)]}: {{topic}}",
        }
        for i in range(n)
    ]


def make_svg_agents(n: int = 10) -> list[dict]:
    return [
        {
            "name": f"Agent {i+1}",
            "emoji": "🎨",
            "color": _COLORS[i % len(_COLORS)],
            "direct_instruction": (
                f"Draw a simple SVG of a {{topic}}. "
                f"Use a {_SVG_STYLES[i % len(_SVG_STYLES)]} style. "
                f"Output SVG only and start with <svg"
            ),
        }
        for i in range(n)
    ]


def make_code_agents(n: int = 10) -> list[dict]:
    return [
        {
            "name": _CODE_LANGS[i % len(_CODE_LANGS)],
            "emoji": _CODE_EMOJIS[i % len(_CODE_EMOJIS)],
            "color": _COLORS[i % len(_COLORS)],
            "direct_instruction": f"Write a solution for {{topic}} in {_CODE_LANGS[i % len(_CODE_LANGS)]}. Output ONLY code.",
        }
        for i in range(n)
    ]


def make_ascii_agents(n: int = 10) -> list[dict]:
    return [
        {
            "name": f"Agent {i+1}",
            "emoji": "👾",
            "color": _COLORS[i % len(_COLORS)],
            "direct_instruction": (
                f"Create ASCII art of {{topic}}. "
                f"Output ASCII art only."
            ),
        }
        for i in range(n)
    ]





# ─── System Prompts ─────────────────────────────────────────

TRANSLATE_SYSTEM = (
    "You are a translator. Output ONLY the translated text. "
    "No explanations, no preamble, no original text, no quotes."
)

SVG_SYSTEM = (
    "You are an SVG artist. Output ONLY a raw <svg> tag with viewBox='0 0 120 120'. "
    "Use vibrant colors. No explanations, no markdown, no text before or after the SVG."
)

CODE_SYSTEM = (
    "You are a programmer. Output ONLY the code. "
    "No explanations, no markdown fences, no language labels. Raw code only."
)

ASCII_SYSTEM = (
    "You are an ASCII artist. Output ONLY raw ASCII art. "
    "No explanations, no markdown fences, no text before or after the art."
)




# ─── Planning Prompts ───────────────────────────────────────

TRANSLATE_PLAN = {
    "system": (
        'Output a JSON array with {n_agents} objects. Each has "name" and "instruction". '
        "Keep each instruction to ONE sentence. Output ONLY valid JSON."
    ),
    "user": (
        'Translate this into {n_agents} languages: "{topic}"\n'
        "Agents: {agent_list}\n"
        'Each instruction: "Translate into [language]: [text]". That is all.'
    ),
}

SVG_PLAN = {
    "system": (
        'Output a JSON array with {n_agents} objects. Each has "name", "instruction", and "label". '
        'The "label" is a short 2-4 word title for the SVG (e.g. "A Cat"). '
        "Output ONLY valid JSON."
    ),
    "user": (
        'Theme: "{topic}". Agents: {agent_list}\n'
        'Each instruction: "Draw a simple SVG of [specific thing].". '
        "One sentence max. Do NOT mention size or format."
    ),
}

CODE_PLAN = {
    "system": (
        'Output a JSON array with {n_agents} objects. Each has "name" and "instruction". '
        "Keep each instruction to ONE sentence. Output ONLY valid JSON."
    ),
    "user": (
        'Task: "{topic}". Agents (each is a programming language): {agent_list}\n'
        'Each instruction: "Write [specific solution] in [language]". One sentence. That is all.'
    ),
}

ASCII_PLAN = {
    "system": (
        'Output a JSON array with {n_agents} objects. Each has "name", "instruction", and "label". '
        'The "label" is a one word description of the ASCII art (e.g. "Cat"). '
        "Output ONLY valid JSON."
    ),
    "user": (
        'Theme: "{topic}". Agents (each is an ASCII artist): {agent_list}\n'
        'Each instruction: "Create realistic and small ASCII (max 20x60 characters) art of [specific aspect of the theme - one word description only]". '
        "One sentence. That is all. "
    ),
}




# ─── Card Renderers ─────────────────────────────────────────
# Each render_card(agent, result) returns ONLY the inner HTML.
# The card wrapper (div, border, hover, padding) is handled by build_page().

def translate_card(agent, result, task=None):
    name = agent["name"]
    emoji = agent["emoji"]
    text = result.strip().strip("`").strip()
    return (
        f'<div class="flex items-center gap-2 mb-3">\n'
        f'    <span class="text-xl">{emoji}</span>\n'
        f'    <span class="text-xs font-semibold text-gray-400 uppercase tracking-wider">{name}</span>\n'
        f'</div>\n'
        f'<div class="text-sm text-gray-700 leading-relaxed">{text}</div>'
    )


def svg_card(agent, result, task=None):
    name = agent["name"]
    label = task.get("label", name.title()) if task else name.title()
    svg = result
    if "<svg" in svg:
        start = svg.index("<svg")
        end = svg.index("</svg>") + 6 if "</svg>" in svg else len(svg)
        svg = svg[start:end]
    else:
        svg = '<div class="text-sm text-gray-400 p-4 text-center">Failed to generate SVG</div>'
    return (
        f'<div class="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-3">{name}</div>\n'
        f'<div class="w-full aspect-square flex items-center justify-center p-2">{svg}</div>\n'
        f'<div class="text-sm font-semibold text-gray-500 mt-3 pt-3 border-t border-gray-200 w-full text-center">{label}</div>'
    )


def code_card(agent, result, task=None):
    name = agent["name"]
    emoji = agent.get("emoji", "💻")
    code = result.strip()
    # Strip markdown fences if present
    if code.startswith("```"):
        lines = code.split("\n")
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        code = "\n".join(lines)
    escaped = html.escape(code)
    lang_class = f'language-{name}' if name in _CODE_LANGS else ''
    return (
        f'<div class="flex items-center gap-2 px-1 pb-3 mb-3 border-b border-gray-200">\n'
        f'    <span class="text-lg">{emoji}</span>\n'
        f'    <span class="text-xs font-semibold text-gray-500 uppercase tracking-wider">{name}</span>\n'
        f'</div>\n'
        f'<pre class="m-0 text-xs leading-relaxed overflow-auto"><code class="{lang_class}" style="padding: 0; background: transparent;">{escaped}</code></pre>'
    )


def ascii_card(agent, result, task=None):
    name = agent["name"]
    label = task.get("label", name.title()) if task else name.title()
    art = result
    if art.startswith("```"):
        lines = art.split("\n")
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        art = "\n".join(lines)
    art = art.strip("\n")
    escaped = html.escape(art)
    return (
        f'<div class="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-3">{name}</div>\n'
        f'<div class="w-full bg-gray-900 rounded-lg p-4 flex items-center justify-center min-h-[180px] overflow-auto">\n'
        f'    <pre class="text-base font-mono text-green-400 leading-tight" style="text-shadow: 0 0 5px rgba(74, 222, 128, 0.5);">{escaped}</pre>\n'
        f'</div>\n'
        f'<div class="text-sm font-semibold text-gray-500 mt-3 pt-3 border-t border-gray-200 w-full text-center">{label}</div>'
    )





# ─── Page Builder ───────────────────────────────────────────

def build_page(topic, scenario, results, tasks=None):
    """Build the full HTML page. Wraps each card automatically."""
    agents = scenario["agents"]
    title = scenario["title"]
    render_card = scenario["render_card"]
    extra_head = scenario.get("extra_head", "")
    extra_body = scenario.get("extra_body", "")

    cols = min((len(agents) + 1) // 2, 5)

    # Build a lookup from agent name → task dict
    task_map = {}
    if tasks:
        for t in tasks:
            task_map[t.get("name", "")] = t

    cards_html = []
    for agent in agents:
        result = results.get(agent["name"], "")
        task = task_map.get(agent["name"])
        inner = render_card(agent, result, task)
        cards_html.append(
            f'            <div class="bg-gray-50 rounded-lg p-4 border border-gray-200 '
            f'hover:shadow-md transition-all">\n'
            f'{inner}\n'
            f'            </div>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; }}
        svg {{ width: 100%; height: 100%; }}
    </style>
{extra_head}
</head>
<body class="bg-white text-gray-900 min-h-screen">
    <div class="mx-auto px-8 py-16" style="max-width: 1920px;">
        <h1 class="text-4xl font-bold text-center mb-2 text-gray-900">
            {title}
        </h1>
        <p class="text-center text-gray-500 text-base mb-12">{topic}</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
{chr(10).join(cards_html)}
        </div>
        <p class="text-center text-gray-400 text-xs mt-12 tracking-wide uppercase">
            Generated by {len(agents)} concurrent Gemma 4 instances
        </p>
    </div>
{extra_body}
</body>
</html>"""


# ─── Scenario Registry ──────────────────────────────────────

SCENARIOS = {
    "translate": {
        "make_agents": make_translate_agents,
        "plan": TRANSLATE_PLAN,
        "system_prompt": TRANSLATE_SYSTEM,
        "render_card": translate_card,
        "title": "Translation Grid",
        "default_n": 10,
    },
    "svg": {
        "make_agents": make_svg_agents,
        "plan": SVG_PLAN,
        "system_prompt": SVG_SYSTEM,
        "render_card": svg_card,
        "title": "SVG Art Gallery",
        "default_n": 10,
    },
    "code": {
        "make_agents": make_code_agents,
        "plan": CODE_PLAN,
        "system_prompt": CODE_SYSTEM,
        "render_card": code_card,
        "title": "Code Gallery",
        "extra_head": (
            '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">\n'
            '    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>'
        ),
        "extra_body": "    <script>hljs.highlightAll();</script>",
        "default_n": 10,
    },
    "ascii": {
        "make_agents": make_ascii_agents,
        "plan": ASCII_PLAN,
        "system_prompt": ASCII_SYSTEM,
        "render_card": ascii_card,
        "title": "ASCII Art Gallery",
        "default_n": 10,
    },

}


def get_scenario(name: str, n_agents: int = None) -> dict:
    """Get a scenario by name. Generates agents dynamically."""
    if name not in SCENARIOS:
        available = ", ".join(SCENARIOS.keys())
        raise KeyError(f"Unknown scenario '{name}'. Available: {available}")
    scenario = dict(SCENARIOS[name])
    n = n_agents or scenario["default_n"]
    scenario["agents"] = scenario["make_agents"](n)
    scenario["plan"] = {
        k: v.replace("{n_agents}", str(n)) if isinstance(v, str) else v
        for k, v in scenario["plan"].items()
    }
    return scenario
