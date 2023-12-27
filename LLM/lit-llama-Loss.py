import numpy as np
from myplotstyle import AcademicPlot
import re

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

log_file = '/data/Data/LeonRho/llm_scripts/lit-llama/lnhang_scripts/log.txt'
iter_nums, losses = parse_log(log_file)

plot = AcademicPlot(figsize=(8,6))
plot.plot(iter_nums, losses)
plot.set_title("Loss Over Iterations")
plot.set_xlabel("Iteration")
plot.set_ylabel("Loss")
plot.savefig('loss.png')
