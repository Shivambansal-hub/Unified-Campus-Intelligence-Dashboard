#!/bin/bash
# start.sh - Launch script for Render deployment
# This script runs all 4 MCP servers in the background, and the Gateway in the foreground.

# Ensure we are executing from the backend directory
cd "$(dirname "$0")"

echo "Starting Library MCP Server on port 8001..."
cd mcp_library
python3 -m uvicorn main:app --host 127.0.0.1 --port 8001 &
cd ..

echo "Starting Cafeteria MCP Server on port 8002..."
cd mcp_cafeteria
python3 -m uvicorn main:app --host 127.0.0.1 --port 8002 &
cd ..

echo "Starting Events MCP Server on port 8003..."
cd mcp_events
python3 -m uvicorn main:app --host 127.0.0.1 --port 8003 &
cd ..

echo "Starting Academics MCP Server on port 8004..."
cd mcp_academics
python3 -m uvicorn main:app --host 127.0.0.1 --port 8004 &
cd ..

echo "Starting API Gateway on port ${PORT:-8000}..."
cd gateway
# Render dynamically assigns a port via the $PORT environment variable.
# We fallback to 8000 for local testing.
PORT=${PORT:-8000}
python3 -m uvicorn main:app --host 0.0.0.0 --port $PORT
