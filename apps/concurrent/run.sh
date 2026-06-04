#!/bin/bash
# ─────────────────────────────────────────────────────────────
# run.sh — Launch the multi-agent demo with Terminal windows.
#
# Opens macOS Terminal windows in a grid layout:
#   - Top row: live throughput dashboard
#   - Grid below: orchestrator + N specialist agents
#
# Usage:
#   bash run.sh --scenario <name> --topic <text> [--port <port>] [--tasks <n>]
#
# Examples:
#   bash run.sh --scenario translate --topic "Hello world"
#   bash run.sh --scenario svg_art --topic "Technology and AI" --tasks 15
# ─────────────────────────────────────────────────────────────

PORT="8080"
SCENARIO="translate"
TOPIC="Gemma is Google DeepMind most capable open AI model"
N_AGENTS=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --port)     PORT="$2";     shift 2 ;;
        --scenario) SCENARIO="$2"; shift 2 ;;
        --topic)    TOPIC="$2";    shift 2 ;;
        --tasks)   N_AGENTS="$2"; shift 2 ;;
        --help)
            echo "Usage: bash run.sh --scenario <name> --topic <text> [--port <port>] [--tasks <n>]"
            echo ""
            echo "Options:"
            echo "  --scenario   Scenario name (translate, svg_art)  [default: translate]"
            echo "  --topic      Topic or text to work on             [required]"
            echo "  --port       llama-server port                    [default: 8080]"
            echo "  --tasks      Number of LLMs to use                [default: scenario default]"
            exit 0 ;;
        *) echo "❌ Unknown argument: $1. Use --help for usage."; exit 1 ;;
    esac
done

# Resolve paths — SCRIPT_DIR is where this script lives (project root)
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
DEMO_DIR="$SCRIPT_DIR/demo"
PYTHON="$SCRIPT_DIR/.venv/bin/python"
API_URL="http://127.0.0.1:${PORT}/v1/chat/completions"

if [ ! -f "$PYTHON" ]; then
    echo "❌ .venv not found at $SCRIPT_DIR/.venv — run 'uv sync' first"
    exit 1
fi

# ─── Load agents from scenario ──────────────────────────────

N_AGENTS_ARG=""
if [ -n "$N_AGENTS" ]; then
    N_AGENTS_ARG=", n_agents=$N_AGENTS"
fi

AGENT_DATA=$("$PYTHON" -c "
import sys
sys.path.insert(0, '$DEMO_DIR')
from scenarios import get_scenario
s = get_scenario('$SCENARIO'${N_AGENTS_ARG})
for a in s['agents']:
    print(f\"{a['name']}|{a['emoji']}|{a['color']}\")
" 2>/dev/null)

if [ -z "$AGENT_DATA" ]; then
    echo "❌ Failed to load scenario '$SCENARIO'"
    exit 1
fi

NAMES=()
EMOJIS=()
COLORS=()
while IFS='|' read -r name emoji color; do
    NAMES+=("$name")
    EMOJIS+=("$emoji")
    COLORS+=("$color")
done <<< "$AGENT_DATA"

NUM_AGENTS=${#NAMES[@]}

# ─── Calculate window layout ────────────────────────────────

bounds=$(osascript -e 'tell application "Finder" to get bounds of window of desktop' 2>/dev/null)
IFS=', ' read -r _ _ SCREEN_X2 SCREEN_Y2 <<< "$bounds"

USABLE_Y1=25
USABLE_Y2=$((SCREEN_Y2 - 120))
USABLE_HEIGHT=$((USABLE_Y2 - USABLE_Y1))

# Dashboard: top 25%
DASH_HEIGHT=$((USABLE_HEIGHT * 25 / 100))
DASH_Y2=$((USABLE_Y1 + DASH_HEIGHT))

# Grid: orchestrator + agents
TOTAL_CELLS=$((NUM_AGENTS + 1))

read COLS GRID_ROWS <<< $("$PYTHON" -c "
import math
n = $TOTAL_CELLS
cols = math.ceil(math.sqrt(n))
rows = math.ceil(n / cols)
print(cols, rows)
")

GRID_Y1=$DASH_Y2
GRID_HEIGHT=$((USABLE_Y2 - GRID_Y1))
ROW_H=$((GRID_HEIGHT / GRID_ROWS))

# ─── Build AppleScript to open windows ──────────────────────

APPLESCRIPT="tell application \"Terminal\"
"

queue_window() {
    APPLESCRIPT+="    set W to do script \"$5\"
    set custom title of window 1 to \"$6\"
    set bounds of window 1 to {$1, $2, $3, $4}
"
}

# Dashboard → top row
dash_cmd="cd \\\"$DEMO_DIR\\\" && \\\"$PYTHON\\\" dashboard.py --server-url 'http://127.0.0.1:${PORT}' --scenario '$SCENARIO' --topic '$TOPIC'"
if [ -n "$N_AGENTS" ]; then
    dash_cmd+=" --tasks $N_AGENTS"
fi
queue_window 0 "$USABLE_Y1" "$SCREEN_X2" "$DASH_Y2" "$dash_cmd" "⚡ Dashboard"

# Orchestrator → first grid cell
orch_cmd="cd \\\"$DEMO_DIR\\\" && \\\"$PYTHON\\\" orchestrator.py --scenario '$SCENARIO' --api-url '$API_URL' --topic '$TOPIC'"
if [ -n "$N_AGENTS" ]; then
    orch_cmd+=" --tasks $N_AGENTS"
fi

# Place orchestrator + agents in grid
for (( i=0; i<TOTAL_CELLS; i++ )); do
    row=$((i / COLS))
    col=$((i % COLS))

    # Last row may have fewer cells — stretch them wider
    if (( row < GRID_ROWS - 1 )); then
        row_count=$COLS
    else
        remainder=$((TOTAL_CELLS % COLS))
        row_count=${remainder:-$COLS}
        if (( row_count == 0 )); then row_count=$COLS; fi
    fi

    win_w=$((SCREEN_X2 / row_count))
    x1=$((col * win_w))
    x2=$(((col + 1) * win_w))
    y1=$((GRID_Y1 + row * ROW_H))
    y2=$((GRID_Y1 + (row + 1) * ROW_H))

    if (( i == 0 )); then
        queue_window "$x1" "$y1" "$x2" "$y2" "$orch_cmd" "🧠 Orchestrator"
    else
        ai=$((i - 1))
        spec_cmd="cd \\\"$DEMO_DIR\\\" && \\\"$PYTHON\\\" specialist.py --name '${NAMES[$ai]}' --emoji '${EMOJIS[$ai]}' --color '${COLORS[$ai]}' --api-url '$API_URL'"
        queue_window "$x1" "$y1" "$x2" "$y2" "$spec_cmd" "${NAMES[$ai]}"
    fi
done

# ─── Launch ────────────────────────────────────────────────

APPLESCRIPT+="end tell"
echo "$APPLESCRIPT" | osascript >/dev/null 2>&1
echo "🚀 Launched: $SCENARIO (${NUM_AGENTS} agents, ${COLS}×${GRID_ROWS} grid + dashboard)"
