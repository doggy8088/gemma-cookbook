"""
dashboard.py — Real-time throughput dashboard for the multi-agent demo.

Uses Rich Live + Layout to display a large hero t/s number alongside
a per-agent compact grid. Reads metrics from .agent_comms/metrics_{name}.json
files written by the orchestrator and specialist agents.

Usage:
    python dashboard.py --server-url http://127.0.0.1:8080 \
        --scenario svg_art [--n-agents 10]
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error

from rich.align import Align
from rich.console import Console, Group
from rich.live import Live
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout

sys.path.insert(0, os.path.dirname(__file__))
from scenarios import get_scenario
from digits import render_big_number
from utils import COMMS_DIR

POLL_INTERVAL = 0.3

# ANSI color code → Rich color mapping
ANSI_TO_RICH = {
    "1;31": "bold red",    "1;32": "bold green",  "1;33": "bold yellow",
    "1;34": "bold blue",   "1;35": "bold magenta", "1;36": "bold cyan",
    "1;37": "bold white",
    "0;31": "red",   "0;32": "green",  "0;33": "yellow",
    "0;34": "blue",  "0;35": "magenta", "0;36": "cyan", "0;37": "white",
}

STATUS_STYLE = {
    "waiting": ("⏳", "dim"),
    "running": ("⚡", "bold green"),
    "done":    ("✅", "bold"),
    "error":   ("❌", "bold red"),
}


def read_agent_metrics(agent_names: list[str]) -> dict[str, dict]:
    """Read all metrics files from .agent_comms/."""
    metrics = {}
    for name in agent_names:
        path = os.path.join(COMMS_DIR, f"metrics_{name}.json")
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    metrics[name] = json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
    return metrics


def fetch_server_metrics(server_url: str) -> dict:
    """Fetch Prometheus metrics from llama-server /metrics endpoint.

    Returns a dict with keys like 'tokens_predicted_per_second', 'tokens_predicted_total', etc.
    Returns empty dict on failure.
    """
    try:
        url = f"{server_url}/metrics"
        req = urllib.request.Request(url, headers={"Accept": "text/plain"})
        with urllib.request.urlopen(req, timeout=1) as resp:
            text = resp.read().decode()
    except (urllib.error.URLError, OSError):
        return {}

    result = {}
    for line in text.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split()
        if len(parts) >= 2:
            key = parts[0]
            try:
                val = float(parts[1])
            except ValueError:
                continue
            result[key] = val
    return result


# ─── Hero Panel (big t/s number) ───────────────────────────

def build_hero(metrics: dict[str, dict], server_metrics: dict = None) -> Panel:
    """Build the large hero panel with the total t/s prominently displayed.

    Sums per-agent t/s for live throughput. Uses server metrics for accurate token counts.
    """
    sum_tps = 0.0
    running = 0
    done = 0
    total_tokens = 0

    for m in metrics.values():
        status = m.get("status", "waiting")
        if status == "running":
            sum_tps += m.get("tps", 0.0)
            running += 1
        elif status == "done":
            done += 1
        total_tokens += m.get("tokens", 0)



    # Large ASCII art number
    big_art = render_big_number(f"{sum_tps:.1f}")
    big_text = Text(big_art, style="bold bright_yellow", justify="left")

    # Status line
    status_parts = []
    if running > 0:
        status_parts.append(f"[bold green]>>> {running} running[/]")
    if done > 0:
        status_parts.append(f"[bold white]<<< {done} done[/]")
    waiting = len(metrics) - running - done
    if len(metrics) == 0:
        status_parts.append("[dim]... waiting for agents ...[/]")
    elif waiting > 0:
        status_parts.append(f"[dim]... {waiting} waiting[/]")
    status_line = Text.from_markup("   ".join(status_parts), justify="center")

    tokens_line = Text.from_markup(
        f"[bright_white]Total tokens: [bold]{total_tokens}[/][/]",
        justify="center"
    )

    content = Group(
        Text(""),
        Align.center(big_text),
        Align.center(Text("tokens / sec", style="bold yellow")),
        Text(""),
        Align.center(Text("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~", style="dim cyan")),
        Text(""),
        Align.center(status_line),
        Align.center(tokens_line),
    )

    return Panel(
        content,
        title="[bold cyan]⚡ THROUGHPUT[/]",
        border_style="cyan",
        padding=(1, 2),
        expand=True,
    )


# ─── Orchestrator Panel ────────────────────────────────────

def build_orchestrator_panel(metrics: dict[str, dict]) -> Panel:
    """Build a compact orchestrator status panel."""
    m = metrics.get("orchestrator", {})
    status = m.get("status", "waiting")
    tokens = m.get("tokens", 0)
    tps = m.get("tps", 0.0)
    elapsed = m.get("elapsed_s", 0.0)

    status_icon, status_style = STATUS_STYLE.get(status, ("❓", "dim"))

    lines = [
        Text.from_markup(
            f"  {status_icon}  Status: [{status_style}]{status.upper()}[/]"
        ),
        Text.from_markup(
            f"  📊  Tokens: [bright_white]{tokens}[/]   "
            f"⏱  [bright_white]{elapsed:.1f}s[/]   "
            f"⚡ [bold bright_yellow]{tps:.1f} t/s[/]"
        ),
    ]

    return Panel(
        Group(*lines),
        title="[bold cyan]ORCHESTRATOR[/]",
        border_style="bright_cyan",
        padding=(0, 1),
        expand=True,
    )


# ─── Agent Grid ────────────────────────────────────────────

def build_agent_card(agent: dict, metrics: dict[str, dict]) -> Text:
    """Build a single compact agent card as a Text renderable."""
    name = agent["name"]
    emoji = agent.get("emoji", "🤖")
    ansi_color = agent.get("color", "1;37")
    rich_color = ANSI_TO_RICH.get(ansi_color, "white")

    m = metrics.get(name, {})
    status = m.get("status", "waiting")
    tps = m.get("tps", 0.0)

    status_icon, _ = STATUS_STYLE.get(status, ("❓", "dim"))

    if status == "running":
        tps_display = f"[bold bright_green]{tps:.1f}[/]"
    elif status == "done":
        tps_display = f"[bright_white]{tps:.1f}[/]"
    else:
        tps_display = "[dim]  — [/]"

    display_name = name.upper().replace("_", " ")
    if len(display_name) > 10:
        display_name = display_name[:9] + "…"

    return Text.from_markup(
        f" {emoji} [{rich_color}]{display_name:<10}[/] {status_icon} {tps_display}"
    )


def build_agent_grid(agents: list[dict], metrics: dict[str, dict], n_cols: int = 3) -> Panel:
    """Build a compact grid of agent mini-cards."""
    sub_agents = [a for a in agents if a["name"] != "orchestrator"]

    if not sub_agents:
        return Panel(
            Align.center(Text("No agents yet...", style="dim")),
            title="[bold cyan]AGENTS[/]",
            border_style="cyan",
            expand=True,
        )

    table = Table(box=None, show_header=False, show_edge=False, padding=(0, 1), expand=True)
    for _ in range(n_cols):
        table.add_column(ratio=1)

    row_cells = []
    for agent in sub_agents:
        row_cells.append(build_agent_card(agent, metrics))
        if len(row_cells) == n_cols:
            table.add_row(*row_cells)
            row_cells = []

    if row_cells:
        while len(row_cells) < n_cols:
            row_cells.append(Text(""))
        table.add_row(*row_cells)

    # Summary
    sum_tps = 0.0
    active_count = 0
    for a in sub_agents:
        m = metrics.get(a["name"], {})
        if m.get("status") == "running":
            sum_tps += m.get("tps", 0.0)
            active_count += 1

    summary = Text.from_markup(
        f"\n  [bold yellow]Σ  {active_count} active agents[/]"
        f"  │  [bold bright_yellow]{sum_tps:.1f} t/s combined[/]"
    )

    return Panel(
        Group(table, summary),
        title="[bold cyan]AGENTS[/]",
        border_style="cyan",
        padding=(0, 0),
        expand=True,
    )


# ─── Combined Layout ──────────────────────────────────────

def build_dashboard(agents: list[dict], metrics: dict[str, dict], server_metrics: dict = None) -> Layout:
    """Assemble the full dashboard layout.

    ┌──────────────┬──────────────────┐
    │              │   ORCHESTRATOR   │
    │  (big t/s)   │                  │
    │              │   AGENT GRID     │
    └──────────────┴──────────────────┘
    """
    layout = Layout()
    layout.split_row(
        Layout(name="hero", ratio=2),
        Layout(name="right", ratio=3),
    )
    layout["right"].split_column(
        Layout(name="orchestrator", size=5),
        Layout(name="agents"),
    )
    layout["hero"].update(build_hero(metrics, server_metrics))
    layout["orchestrator"].update(build_orchestrator_panel(metrics))
    layout["agents"].update(build_agent_grid(agents, metrics))
    return layout


def main():
    parser = argparse.ArgumentParser(description="Real-time throughput dashboard")
    parser.add_argument("--server-url", default="http://127.0.0.1:8080",
                        help="llama-server base URL")
    parser.add_argument("--scenario", default="translate")
    parser.add_argument("--topic", default="Generative AI")
    parser.add_argument("--tasks", type=int, default=None)
    args = parser.parse_args()

    scenario = get_scenario(args.scenario, n_agents=args.tasks)
    agents = scenario["agents"]

    # Add orchestrator to agent list for tracking
    agents.insert(0, {
        "name": "orchestrator",
        "emoji": "🧠",
        "color": "1;36",
    })
    agent_names = [a["name"] for a in agents]

    console = Console()
    console.clear()
    time.sleep(1)

    all_done_since = None
    EXIT_DELAY = 1.0

    with Live(console=console, refresh_per_second=4, screen=True) as live:
        while True:
            now = time.time()
            metrics = read_agent_metrics(agent_names)
            server_metrics = fetch_server_metrics(args.server_url)
            live.update(build_dashboard(agents, metrics, server_metrics))

            # Exit once all agents are done for EXIT_DELAY seconds
            if metrics:
                all_done = (
                    all(
                        metrics.get(name, {}).get("status") == "done"
                        for name in agent_names
                        if name in metrics
                    )
                    and len(metrics) == len(agent_names)
                )
                if all_done:
                    if all_done_since is None:
                        all_done_since = now
                    elif (now - all_done_since) >= EXIT_DELAY:
                        break
                else:
                    all_done_since = None

            time.sleep(POLL_INTERVAL)

    # Final summary
    console.clear()
    metrics = read_agent_metrics(agent_names)
    server_metrics = fetch_server_metrics(args.server_url)
    total_tokens = sum(m.get("tokens", 0) for m in metrics.values())
    total_time = max(m.get("elapsed_s", 0) for m in metrics.values()) if metrics else 0
    sum_tps = sum(m.get("tps", 0) for m in metrics.values())



    summary_lines = [
        "[bold green]✅ All agents complete![/]\n",
        f"  [bright_white]Total tokens generated:[/] [bold]{total_tokens}[/]",
        f"  [bright_white]Wall-clock time:[/] [bold]{total_time:.1f}s[/]",
        f"  [bright_white]Parallel throughput:[/] [bold bright_yellow]{sum_tps:.1f} t/s[/]",
    ]
    if total_time > 0:
        effective = total_tokens / total_time
        summary_lines.append(
            f"  [bright_white]Effective throughput:[/] [bold bright_cyan]{effective:.1f} t/s[/]"
        )

    console.print(Panel(
        "\n".join(summary_lines),
        title="[bold cyan]⚡ Final Summary[/]",
        border_style="cyan",
        padding=(1, 2),
    ))

    input("\nPress Enter to close...")


if __name__ == "__main__":
    main()
