#!/bin/bash

# 获得scripts目录的路径
WORK_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
SCRIPTS_PATH="$WORK_PATH"

# 检查scripts目录是否存在
if [ -d "$SCRIPTS_PATH" ]; then
    echo "Found scripts directory: $SCRIPTS_PATH"
    export PYTHONPATH=$SCRIPTS_PATH:$PYTHONPATH
    echo "PYTHONPATH updated to include scripts directory."
else
    echo "Scripts directory not found: $SCRIPTS_PATH"
fi
