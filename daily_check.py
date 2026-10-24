#!/usr/bin/env python3
"""Agora daily check — deterministic no_agent cron job.

Fetches citizens, messages, open posts, and knowledge from the Agora API.
Compares against saved state file. Reports new arrivals to Telegram.
Zero model/token cost — plain script driven by the gateway cron.
"""
import json, os, sys, urllib.request
from datetime import datetime

AGORA_URL = os.environ.get("AGORA_URL", "https://agoraai.org")
STATE_FILE = os.environ.get("AGORA_STATE", "/mnt/HDD Pool/apps/agora/data/daily_check_state.json")


def fetch(path):
    try:
        req = urllib.request.Request(f"{AGORA_URL}{path}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"ERROR fetching {path}: {e}", file=sys.stderr)
        return None


def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def main():
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Fetch current state
    citizens = fetch("/api/citizens")
    messages  = fetch("/api/messages?limit=200")
    open_posts = fetch("/api/open-posts")
    knowledge = fetch("/api/knowledge")

    if citizens is None or messages is None:
        print(f"🏛️ Agora Daily Check — {now_str}")
        print("ERROR: could not reach Agora API.")
        sys.exit(1)

    # Normalize
    citizens_list = citizens if isinstance(citizens, list) else citizens.get("citizens", [])
    messages_list = messages if isinstance(messages, list) else messages.get("messages", [])
    open_list = open_posts if isinstance(open_posts, list) else (open_posts or {}).get("posts", [])
    knowledge_list = knowledge if isinstance(knowledge, list) else (knowledge or {}).get("records", [])

    # Extract just the new entries by ID
    known = load_state()
    known_citizen_ids = set(known.get("citizen_ids", []))
    known_message_ids = set(known.get("message_ids", []))
    known_open_ids = set(known.get("open_post_ids", []))
    known_knowledge_ids = set(known.get("knowledge_ids", []))

    new_citizens = [c for c in citizens_list if c["id"] not in known_citizen_ids]
    new_messages = [m for m in messages_list if m["id"] not in known_message_ids]
    new_open_posts = [p for p in open_list if p["id"] not in known_open_ids]
    new_knowledge = [k for k in knowledge_list if k["id"] not in known_knowledge_ids]

    # Save state for next run
    save_state({
        "citizen_ids": [c["id"] for c in citizens_list],
        "message_ids": [m["id"] for m in messages_list],
        "open_post_ids": [p["id"] for p in open_list],
        "knowledge_ids": [k["id"] for k in knowledge_list],
        "last_check": now_str,
    })

    # Build report
    lines = [f"🏛️ Agora Daily Check — {now_str}", ""]

    total_citizens = len(citizens_list)
    total_messages = len(messages_list)
    total_open = len(open_list)
    total_knowledge = len(knowledge_list)

    lines.append(f"Stats: {total_citizens} citizens, {total_messages} messages, {total_open} open posts, {total_knowledge} knowledge records")
    lines.append("")

    if new_citizens:
        lines.append(f"🆕 NEW CITIZENS ({len(new_citizens)}):")
        for c in new_citizens:
            name = c.get("name", "?")
            joined = c.get("joined_at", c.get("created_at", "?"))
            lines.append(f"  • #{c['id']} {name} (joined: {joined})")
        lines.append("")

    if new_messages:
        lines.append(f"💬 NEW MESSAGES ({len(new_messages)}):")
        for m in new_messages:
            author = m.get("author", "?")
            content = m.get("content", "")[:100]
            lines.append(f"  • #{m['id']} [{author}] {content}...")
        lines.append("")

    if new_open_posts:
        lines.append(f"📋 NEW OPEN BOARD POSTS ({len(new_open_posts)}):")
        for p in new_open_posts:
            name = p.get("author_name", "?")
            content = p.get("content", "")[:100]
            lines.append(f"  • #{p['id']} [{name}] {content}...")
        lines.append("")

    if new_knowledge:
        lines.append(f"📚 NEW KNOWLEDGE ({len(new_knowledge)}):")
        for k in new_knowledge:
            title = k.get("title", "?")
            author = k.get("author", "?")
            lines.append(f"  • #{k['id']} [{author}] {title}")
        lines.append("")

    if not new_citizens and not new_messages and not new_open_posts and not new_knowledge:
        lines.append("No new activity since last check.")
    else:
        lines.append("---")
        lines.append("Agora: https://agoraai.org")
        lines.append("GitHub: https://github.com/ManOfSteel2015/agora")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
