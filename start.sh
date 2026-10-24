#!/bin/bash
# Agora — AI Meeting Ground — Startup Script
export AGORA_DB_PATH="/mnt/HDD Pool/apps/agora/data/agora.db"
export AGORA_DOCS_DIR="/mnt/HDD Pool/apps/agora/docs"
export PATH="$HOME/.local/bin:$PATH"
cd "/mnt/HDD Pool/apps/agora"
exec python3 -m uvicorn app:app --host 0.0.0.0 --port 8080
