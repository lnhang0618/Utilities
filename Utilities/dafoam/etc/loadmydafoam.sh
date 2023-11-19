#!/bin/bash

# 获取脚本所在的目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 设置 plot 脚本的路径
PLOT_PATH="$SCRIPT_DIR/scripts/plot"
export PATH="$PLOT_PATH:$PATH"

# 设置 createSDict 脚本的路径
CREATESDICT_PATH="$SCRIPT_DIR/scripts/createSDict"
export PATH="$CREATESDICT_PATH:$PATH"
