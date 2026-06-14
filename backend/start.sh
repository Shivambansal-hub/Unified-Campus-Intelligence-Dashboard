#!/bin/bash
# start.sh - Launch script for Render deployment
# This script runs all 4 MCP servers in the background, and the Gateway in the foreground.
set -e

# Get the absolute path of this script's directory (backend/)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Starting Library MCP Server on port 8001..."
cd "$SCRIPT_DIR/mcp_library"
python3 -m uvicorn main:app --host 127.0.0.1 --port 8001 &

echo "Starting Cafeteria MCP Server on port 8002..."
cd "$SCRIPT_DIR/mcp_cafeteria"
python3 -m uvicorn main:app --host 127.0.0.1 --port 8002 &

echo "Starting Events MCP Server on port 8003..."
cd "$SCRIPT_DIR/mcp_events"
python3 -m uvicorn main:app --host 127.0.0.1 --port 8003 &

echo "Starting Academics MCP Server on port 8004..."
cd "$SCRIPT_DIR/mcp_academics"
python3 -m uvicorn main:app --host 127.0.0.1 --port 8004 &

# Give MCP servers a moment to boot before starting the gateway
sleep 2

echo "Starting API Gateway on port ${PORT:-8000}..."
cd "$SCRIPT_DIR/gateway"
PORT=${PORT:-8000}
exec python3 -m uvicorn main:app --host 0.0.0.0 --port "$PORT"
