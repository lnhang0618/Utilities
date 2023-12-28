import numpy as np
import re
import yaml
from sciplotlib import AcademicPlot
import sys
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset

# 示例代码
def print_yaml_example():
    yaml_example = """
    log_files:
      - path: "path/to/log1.txt"
        label: "Experiment 1"
      - path: "path/to/log2.txt"
        label: "Experiment 2"
    sampling_rate: 10
    window_size: 5
    plot_setting:
      x_lim: [0, 5000]
      y_lim: [0, 5]
    inset:
        zoom: 2
        loc: 1
        x1: 1000
        x2: 3000
        y1: 1
        y2: 3
    """
    print("YAML配置文件示例:")
    print(yaml_example)



# 修改这个函数来解析YAML文件
def parse_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def parse_log(file_path, sampling_rate=1, window_size=5):
    iter_nums = []
    raw_losses = []
    smoothed_losses = []
    counter = 0

    with open(file_path, 'r') as file:
        for line in file:
            if counter % sampling_rate == 0:
                match = re.search(r'iter (\d+): loss (\d+\.\d+)', line)
                if match:
                    iter_num = int(match.group(1))
                    loss = float(match.group(2))
                    iter_nums.append(iter_num)
                    raw_losses.append(loss)
                    
                    # 计算移动平均
                    if len(raw_losses) < window_size:
                        # 如果还没有足够的点来填满窗口，则取目前所有点的平均
                        smoothed_loss = np.mean(raw_losses)
                    else:
                        # 否则，取最近的window_size个点的平均
                        smoothed_loss = np.mean(raw_losses[-window_size:])
                    
                    smoothed_losses.append(smoothed_loss)
            counter += 1

    return iter_nums, smoothed_losses

if __name__ == "__main__":
    # 接受一个YAML配置文件的路径
    if len(sys.argv) > 1:
        yaml_file_path = sys.argv[1]
    else:
        print("Usage: python script_name.py <path to YAML file>")
        print_yaml_example()
        sys.exit(1)  # 当没有提供YAML文件时退出

    config = parse_yaml(yaml_file_path)

    log_files=config['log_files']
    sampling_rate=config['sampling_rate']
    window_size=config.get('window_size',5)
    plot_setting=config.get('plot_setting',{})

    plot = AcademicPlot(figsize=(8, 6))

    # 在循环开始之前创建放大区域
    axins = zoomed_inset_axes(plot.ax, zoom=config['inset'].get('zoom',2), loc=config['inset'].get('loc',1))
    for file_config in log_files:
        file_path = file_config['path']
        label = file_config['label']
        iter_nums, losses = parse_log(file_path, sampling_rate=sampling_rate, window_size=window_size)
        
        # 在主轴上绘制每条线
        plot.plot(iter_nums, losses, label=label)
        
        # 在放大区域绘制每条线
        axins.plot(iter_nums, losses)

    # 设置放大区域的坐标轴范围
    x1, x2, y1, y2 = config['inset'].get('x1',500), config['inset'].get('x2',2500), config['inset'].get('y1',2.5), config['inset'].get('y2',4)
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    axins.yaxis.set_visible(False)
    axins.xaxis.set_visible(False)

    # 在主轴上标记放大区域
    mark_inset(plot.ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

    # 显示图例

    if plot_setting.get('x_lim',None) is not None:
        plot.ax.set_xlim(plot_setting['x_lim'][0],plot_setting['x_lim'][1])
    if plot_setting.get('y_lim',None) is not None:
        plot.ax.set_ylim(plot_setting['y_lim'][0],plot_setting['y_lim'][1])
    
    plot.legend(ax=plot.ax,loc='upper left')

    plot.show()

    # 保存图片到一个固定的文件名
    plot.savefig('./assets/combined_loss.png')

