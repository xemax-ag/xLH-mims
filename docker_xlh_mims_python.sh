#!/bin/bash
#set -xe
clear

if [[ "${MODE:-}" == "jupyterlab" ]]; then
  jupyter-lab --ip=0.0.0.0 --allow-root --NotebookApp.token='' --notebook-dir="notebooks"
elif [[ "${MODE:-}" == "api" ]]; then
  shell_dir="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
  cd "$shell_dir"
  source .venv/bin/activate
  uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8099
else
  echo "Unknown MODE: ${MODE:-unset}"
fi