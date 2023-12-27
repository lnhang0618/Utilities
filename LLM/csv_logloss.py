import numpy as np
import re
import yaml
from sciplotlib import AcademicPlot
import sys
import csv

# 修改这个函数来解析YAML文件
def parse_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def parse_log(file_path, sampling_rate=1):
    iter_nums = []
    losses = []
    counter = 0  # 添加一个计数器用于实现采样

    with open(file_path, newline='') as file:
        log_reader = csv.DictReader(file)
        next(log_reader, None)
        for row in log_reader:
            if counter % sampling_rate == 0:  # 每隔sampling_rate个样本点取一个数据点
                if len(row) >= 2:
                    try:
                        iter_num = int(row['iter'])
                        loss = float(row['val_loss'])
                        if loss == config.get('skip_loss',-1):
                            continue
                        else:
                            iter_nums.append(iter_num)
                            losses.append(loss)
                    except ValueError:
                        # 处理转换异常，例如无效的整数或浮点数
                        continue
            counter += 1


    print("len(losses):",len(losses))
    print("len(iter_nums):",len(iter_nums))
    return iter_nums, losses

if __name__ == "__main__":
    # 接受一个YAML配置文件的路径
    if len(sys.argv) > 1:
        yaml_file_path = sys.argv[1]
    else:
        print("Usage: python script_name.py <path to YAML file>")
        sys.exit(1)  # 当没有提供YAML文件时退出

    config = parse_yaml(yaml_file_path)

    log_files=config['log_files']
    sampling_rate=config['sampling_rate']
    plot_setting=config.get('plot_setting',{})

    plot = AcademicPlot(figsize=(8, 6))

    for file_config in log_files:
        file_path = file_config['path']
        label = file_config['label']
        iter_nums, losses = parse_log(file_path,sampling_rate=sampling_rate)
        plot.plot(iter_nums, losses, label=label)  # 使用自定义标签

    plot.set_title("Loss Over Iterations")
    plot.set_xlabel("Iteration")
    plot.set_ylabel("Loss")
    plot.enable_scientific_notation(axis='both')

    if plot_setting.get('x_lim',None) is not None:
        plot.ax.set_xlim(plot_setting['x_lim'][0],plot_setting['x_lim'][1])
    if plot_setting.get('y_lim',None) is not None:
        plot.ax.set_ylim(plot_setting['y_lim'][0],plot_setting['y_lim'][1])

    plot.show()

    # 保存图片到一个固定的文件名
    plot.savefig('./assets/combined_val_loss.png')

