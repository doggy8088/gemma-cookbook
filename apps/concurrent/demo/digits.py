"""
digits.py — ASCII art font for the real-time throughput dashboard.
"""

# ─────────────────────────────────────────────────────────────
# Font: "Shaded" blocks (7 lines tall, 10 chars wide per glyph)
# ─────────────────────────────────────────────────────────────

GLYPHS = {
    "0": [
        " ░██████ ",
        "░██   ░██",
        "░██   ░██",
        "░██   ░██",
        "░██   ░██",
        "░██   ░██",
        " ░██████ ",
    ],
    "1": [
        "  ░██  ",
        "░████  ",
        "  ░██  ",
        "  ░██  ",
        "  ░██  ",
        "  ░██  ",
        "░██████",
    ],
    "2": [
        " ░██████ ",
        "░██   ░██",
        "      ░██",
        "  ░█████ ",
        " ░██     ",
        "░██      ",
        "░████████",
    ],
    "3": [
        " ░██████ ",
        "░██   ░██",
        "      ░██",
        "  ░█████ ",
        "      ░██",
        "░██   ░██",
        " ░██████ ",
    ],
    "4": [
        "   ░████ ",
        "  ░██ ██ ",
        " ░██  ██ ",
        "░██   ██ ",
        "░█████████",
        "     ░██ ",
        "     ░██ ",
    ],
    "5": [
        "░████████",
        "░██      ",
        "░███████ ",
        "      ░██",
        "░██   ░██",
        "░██   ░██",
        " ░██████ ",
    ],
    "6": [
        " ░██████ ",
        "░██   ░██",
        "░██      ",
        "░███████ ",
        "░██   ░██",
        "░██   ░██",
        " ░██████ ",
    ],
    "7": [
        "░█████████",
        "░██    ░██",
        "      ░██ ",
        "     ░██  ",
        "    ░██   ",
        "    ░██   ",
        "    ░██   ",
    ],
    "8": [
        " ░██████ ",
        "░██   ░██",
        "░██   ░██",
        " ░██████ ",
        "░██   ░██",
        "░██   ░██",
        " ░██████ ",
    ],
    "9": [
        " ░██████ ",
        "░██   ░██",
        "░██   ░██",
        " ░███████",
        "      ░██",
        "░██   ░██",
        " ░██████ ",
    ],
    ".": [
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        " ░████   ",
    ],
}

# Pad every row to exactly 10 characters to prevent alignment jitter
GLYPHS = {k: [r.ljust(10) for r in v] for k, v in GLYPHS.items()}

_HEIGHT = 7


def render_big_number(number_str: str) -> str:
    """Render a number string as shaded block characters."""
    lines = [""] * _HEIGHT
    for ch in number_str:
        glyph = GLYPHS.get(ch)
        if glyph is None:
            width = len(GLYPHS["0"][0])
            glyph = [" " * width] * _HEIGHT
        for i in range(_HEIGHT):
            lines[i] += glyph[i]
    return "\n".join(lines)
