#!/bin/bash

# 第一个 load 脚本的相对路径（相对于主目录）
LOAD_SCRIPT_DAFOAM_REL_PATH="dafoam/loadmydafoam.sh"

# 第二个 load 脚本的相对路径
LOAD_SCRIPT_PLOT_REL_PATH="sciplotlib/loadmyplot.sh"

# ~/.bashrc 文件的路径
BASHRC="$HOME/.bashrc"

# 检查~/.bashrc中是否已存在相应的source命令
# 对于 loadmydafoam.sh
if ! grep -q "source $(pwd)/$LOAD_SCRIPT_DAFOAM_REL_PATH" "$BASHRC"; then
    echo "source $(pwd)/$LOAD_SCRIPT_DAFOAM_REL_PATH" >> "$BASHRC"
    echo "Added 'source $(pwd)/$LOAD_SCRIPT_DAFOAM_REL_PATH' to $BASHRC"
else
    echo "'source $(pwd)/$LOAD_SCRIPT_DAFOAM_REL_PATH' already in $BASHRC"
fi

# 对于 loadmyplot.sh
if ! grep -q "source $(pwd)/$LOAD_SCRIPT_PLOT_REL_PATH" "$BASHRC"; then
    echo "source $(pwd)/$LOAD_SCRIPT_PLOT_REL_PATH" >> "$BASHRC"
    echo "Added 'source $(pwd)/$LOAD_SCRIPT_PLOT_REL_PATH' to $BASHRC"
else
    echo "'source $(pwd)/$LOAD_SCRIPT_PLOT_REL_PATH' already in $BASHRC"
fi
