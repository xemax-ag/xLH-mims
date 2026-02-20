#!/bin/bash
#set -xe
clear
shell_dir="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
cd "$shell_dir"
source .venv/bin/activate
uvicorn app.main:app \
  --host 0.0.0.0 \
  --port 8099 \
  --reload \
  --reload-dir="app"