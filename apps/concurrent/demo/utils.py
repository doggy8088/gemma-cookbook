"""
utils.py — Shared utilities for the multi-agent demo.

Contains the LLM streaming logic, metrics writer, and shared constants
used by both the orchestrator and specialist agents.
"""

import json
import os
import sys
import time

from openai import OpenAI

# ─── Shared Paths ───────────────────────────────────────────

COMMS_DIR = os.path.join(os.path.dirname(__file__), ".agent_comms")
BUILD_DIR = os.path.join(os.path.dirname(__file__), "website_build")

# ─── ANSI Colors ────────────────────────────────────────────

RESET = "\033[0m"
DIM = "\033[2m"
BOLD = "\033[1m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"


# ─── Metrics ────────────────────────────────────────────────

def write_metrics(name: str, status: str, tokens: int, elapsed: float, tps: float = None):
    """Write metrics to .agent_comms/metrics_{name}.json atomically."""
    if tps is None:
        tps = tokens / elapsed if elapsed > 0 else 0.0
    metrics = {
        "name": name,
        "status": status,
        "tokens": tokens,
        "elapsed_s": round(elapsed, 2),
        "tps": round(tps, 1),
    }
    path = os.path.join(COMMS_DIR, f"metrics_{name}.json")
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(metrics, f)
    os.replace(tmp, path)


# ─── LLM Streaming ─────────────────────────────────────────

def stream_llm(
    api_url: str,
    messages: list[dict],
    agent_name: str,
    color: str = "1;37",
    max_tokens: int = 4000,
) -> str:
    """Stream an LLM response, update metrics, and print tokens in color.

    Args:
        api_url:    Full chat completions URL (e.g. http://…/v1/chat/completions).
        messages:   OpenAI-style messages list.
        agent_name: Name used for metrics files.
        color:      ANSI color code for terminal output.
        max_tokens: Maximum tokens to generate.

    Returns:
        The full response text (content only, excluding reasoning tokens).
    """
    base_url = api_url.rsplit("/chat/completions", 1)[0]
    client = OpenAI(base_url=base_url, api_key="sk-no-key")

    full = ""
    chunk_count = 0
    server_tokens = None  # Will be set from usage if available
    start_t = time.time()

    try:
        write_metrics(agent_name, "running", 0, 0.0, 0.0)

        last_poll_t = start_t
        poll_interval = 0.3
        chunks_since_poll = 0

        response = client.chat.completions.create(
            model="default",
            messages=messages,
            max_tokens=max_tokens,
            stream=True,
            stream_options={"include_usage": True},
        )

        for chunk in response:
            # Final chunk with usage stats (no choices)
            if hasattr(chunk, "usage") and chunk.usage:
                server_tokens = chunk.usage.completion_tokens
                continue

            if not chunk.choices:
                continue
            delta = chunk.choices[0].delta

            # Handle reasoning tokens (thinking models)
            rc = getattr(delta, "reasoning_content", None)
            if rc:
                sys.stdout.write(f"\033[2;37m{rc}\033[0m")
                sys.stdout.flush()

            c = delta.content or ""
            if c:
                full += c
                sys.stdout.write(f"\033[{color}m{c}\033[0m")
                sys.stdout.flush()

            if rc or c:
                chunks_since_poll += 1
                chunk_count += 1

                now = time.time()
                if (now - last_poll_t) >= poll_interval:
                    tps = chunks_since_poll / (now - last_poll_t)
                    tokens = server_tokens if server_tokens is not None else chunk_count
                    write_metrics(agent_name, "running", tokens, now - start_t, tps)
                    chunks_since_poll = 0
                    last_poll_t = now

    except Exception as e:
        sys.stdout.write(f"\n\033[31m[ERROR] {e}\033[0m\n")

    total_elapsed = time.time() - start_t
    # Use server-reported token count if available, otherwise fall back to chunk count
    final_tokens = server_tokens if server_tokens is not None else chunk_count
    final_tps = final_tokens / total_elapsed if total_elapsed > 0 else 0.0
    write_metrics(agent_name, "done", final_tokens, total_elapsed, final_tps)

    return full
