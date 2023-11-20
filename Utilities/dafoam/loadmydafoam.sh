#!/bin/bash

# 获得scripts目录的路径
WORK_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
SCRIPTS_PATH="$WORK_PATH/scripts"

# 检查scripts目录是否存在
if [ -d "$SCRIPTS_PATH" ]; then
    echo "Found scripts directory: $SCRIPTS_PATH"
    export PATH=$SCRIPTS_PATH:$PATH
    echo "PATH updated to include scripts directory."
else
    echo "Scripts directory not found: $SCRIPTS_PATH"
fi

# 输出新的PATH以供检查
echo "Current PATH: $PATH"
