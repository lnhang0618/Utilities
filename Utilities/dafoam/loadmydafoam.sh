#!/bin/bash

# 输出当前工作目录
echo "Current working directory: $(pwd)"

# 设置脚本路径
scripts_PATH=$(pwd)/scripts/

# 检查scripts目录是否存在
if [ -d "$scripts_PATH" ]; then
    echo "Found scripts directory: $scripts_PATH"
    export PATH=$scripts_PATH:$PATH
    echo "PATH updated to include scripts directory."
else
    echo "Scripts directory not found: $scripts_PATH"
fi

# 输出新的PATH以供检查
echo "Current PATH: $PATH"
