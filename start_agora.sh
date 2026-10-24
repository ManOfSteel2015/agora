#!/bin/bash
# Agora autostart — runs uvicorn + cloudflared tunnel on boot
cd "/mnt/HDD Pool/apps/agora"

# Kill any existing instances
pkill -f "uvicorn app:app" 2>/dev/null
sleep 2

# Start uvicorn
AGORA_DB_PATH="/mnt/HDD Pool/apps/agora/data/agora.db" \
AGORA_DOCS_DIR="/mnt/HDD Pool/apps/agora/docs" \
nohup python3 -m uvicorn app:app --host 0.0.0.0 --port 8080 > "/mnt/HDD Pool/apps/agora/server.log" 2>&1 &

sleep 5

# Start cloudflared tunnel
nohup ./cloudflared tunnel run agora >> "/mnt/HDD Pool/apps/agora/tunnel-named.log" 2>&1 &

echo "Agora started"
