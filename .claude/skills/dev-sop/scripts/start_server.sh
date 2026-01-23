#!/bin/bash
# Quick runs in background server starter -
# Usage: ./start_server.sh [port] [directory]
# Default: port 2527, current directory

PORT=${1:-2527}
DIR=${2:-.}
PORT_IN_USE=$(lsof -ti:$PORT 2>/dev/null)

if [ ! -z "$PORT_IN_USE" ]; then
    echo "⚠️  Port $PORT is in use. Kill it? (y/n)"
    read -r answer
    if [ "$answer" = "y" ]; then
        kill $PORT_IN_USE
        echo "✅ Killed process on port $PORT"
    else
        echo "❌ Aborted"
        exit 1
    fi
fi

cd "$DIR" && python3 -m http.server $PORT &
echo "🚀 Server started on http://localhost:$PORT"
echo "📂 Serving: $(pwd)"
