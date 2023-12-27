import numpy as np
from myplotstyle import AcademicPlot
import re
import sys

# 检查是否有命令行参数传入
if len(sys.argv) > 1:
    file_path = sys.argv[1]  # 使用命令行指定的文件
else:
    file_path = './log.txt'  # 如果没有指定文件，则在当前目录查找opt_IPOPT.txt


def parse_log(file_path):
    iter_nums = []
    losses = []

    with open(file_path, 'r') as file:
        for line in file:
            print("Processing line:", line.strip())  # 打印当前处理的行

            match = re.search(r'iter (\d+): loss (\d+\.\d+)', line)
            if match:
                iter_num = int(match.group(1))
                loss = float(match.group(2))
                iter_nums.append(iter_num)
                losses.append(loss)
            else:
                print("No match found in line:", line.strip())  # 如果没有匹配到，则打印这一行

    return iter_nums, losses

if __name__ == "__main__":
    iter_nums, losses = parse_log(file_path)

    plot = AcademicPlot(figsize=(8,6))
    plot.plot(iter_nums, losses)
    plot.set_title("Loss Over Iterations")
    plot.set_xlabel("Iteration")
    plot.set_ylabel("Loss")
    plot.enable_scientific_notation(axis='both')

    plot.show()
    plot.savefig('loss.png')
