#!/bin/bash

# loadxxx.sh 的相对路径（相对于主目录）
LOAD_SCRIPT_REL_PATH="dafoam/loadmydafoam.sh"

# ~/.bashrc 文件的路径
BASHRC="$HOME/.bashrc"

# 检查~/.bashrc中是否已存在相应的source命令
if ! grep -q "source $(pwd)/$LOAD_SCRIPT_REL_PATH" "$BASHRC"; then
    # 如果不存在，就将source命令追加到~/.bashrc文件的末尾
    echo "source $(pwd)/$LOAD_SCRIPT_REL_PATH" >> "$BASHRC"
    echo "Added 'source $(pwd)/$LOAD_SCRIPT_REL_PATH' to $BASHRC"
else
    echo "'source $(pwd)/$LOAD_SCRIPT_REL_PATH' already in $BASHRC"
fi

