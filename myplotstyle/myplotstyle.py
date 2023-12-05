import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator,AutoMinorLocator

# 设置字体和启用 LaTeX
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = True


'''
Google Colab 
#f44336 (红色)
#e91e63 (桃红色)
#9c27b0 (深紫色)
#673ab7 (靛蓝色)
#3f51b5 (蓝色)
#2196f3 (亮蓝色)
#03a9f4 (天蓝色)
#00bcd4 (青色)
#009688 (蓝绿色)
#4caf50 (绿色)
'''

'''
Tableau
#1f77b4 (蓝色)
#ff7f0e (橙色)
#2ca02c (绿色)
#d62728 (红色)
#9467bd (紫色)
#8c564b (棕色)
#e377c2 (粉红色)
#7f7f7f (灰色)
#bcbd22 (黄绿色)
#17becf (青色)
'''

class AcademicPlot(object):
    default_line_styles = ['-', '--', '-.', ':','solid','dashed','dashdot','dotted']
    default_line_marker = ['H', 'v', '<', '>', 'D', 'd', 'X', 'x']
    default_line_colors = ['#1f77b4','#e377c2', '#ff7f0e', '#2ca02c', '#9467bd', '#8c564b', '#7f7f7f ','#bcbd22']
    default_scatter_colors = ['#d62728','#17becf']
    default_scatter_markers = ['^', 'o', 's', 'p', 'P']
    default_markevery = 10
    default_markersize = 10

    def __init__(self, ax=None, figsize=(4, 3), tick_count=5,default_frontsize = 20):
        if ax is None:
            self.fig, self.ax = plt.subplots(figsize=figsize)
        else:
            self.fig = ax.get_figure()
            self.ax = ax
        self.default_frontsize = default_frontsize
        self.set_base_style(tick_count)
        self.line_count = 0
        self.scatter_count = 0


    def set_base_style(self, tick_count):
        self.ax.spines['top'].set_visible(True)
        self.ax.spines['right'].set_visible(True)
        self.ax.xaxis.set_major_locator(MaxNLocator(tick_count))
        self.ax.yaxis.set_major_locator(MaxNLocator(tick_count))
        
        # 设置主刻度的大小和方向
        self.ax.tick_params(axis='both', which='major', length=10, width=2, direction='in')

        # 设置次刻度的大小和方向
        self.ax.tick_params(axis='both', which='minor', length=5, width=1, direction='in')
        
        # 设置 x 轴和 y 轴刻度标签的字体大小
        for label in self.ax.get_xticklabels():
            label.set_fontsize(self.default_frontsize)
        for label in self.ax.get_yticklabels():
            label.set_fontsize(self.default_frontsize)
            
        # 添加次刻度，但不显示刻度标签
        self.ax.xaxis.set_minor_locator(AutoMinorLocator())
        self.ax.yaxis.set_minor_locator(AutoMinorLocator())

        # 隐藏次刻度的标签
        for label in self.ax.xaxis.get_minorticklabels():
            label.set_visible(False)
        for label in self.ax.yaxis.get_minorticklabels():
            label.set_visible(False)

    def set_labels(self, title="", xlabel="", ylabel=""):
        self.ax.set_title(title, fontsize=self.default_frontsize)
        self.ax.set_xlabel(xlabel, fontsize=self.default_frontsize)
        self.ax.set_ylabel(ylabel, fontsize=self.default_frontsize)

    def plot_scatter(self, x, y, label=None,marker=None, color=None, is_filled=True):
        if marker is None:
            marker = self.default_scatter_markers[self.scatter_count % len(self.default_scatter_markers)]
        if color is None:
            color = self.default_scatter_colors[self.scatter_count % len(self.default_scatter_colors)]
        facecolor = color if is_filled else 'none'
        self.ax.scatter(x, y, marker=marker, color=color, facecolor=facecolor, label=label, s=self.default_markersize*20)
        self.scatter_count += 1

    def plot_line(self, x, y, label=None, linestyle=None, linewidth=2, color=None, marker=None, markevery=None):
        if linestyle is None:
            linestyle = self.default_line_styles[self.line_count % len(self.default_line_styles)]
        if color is None:
            color = self.default_line_colors[self.line_count % len(self.default_line_colors)]
        if marker is None:
            marker = self.default_line_marker[self.line_count % len(self.default_line_marker)]
        if markevery is None:
            markevery = self.default_markevery
        self.ax.plot(x, y, linestyle=linestyle,linewidth=linewidth, color=color, marker=marker, markevery=markevery,label=label,markersize=self.default_markersize)
        self.line_count += 1
        
    def plot_contour(self, X, Y, Z, cmap='jet', levels=100, colorbar_label=''):
        # 绘制等高线图
        contour = self.ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
        # 添加颜色条
        cbar = self.fig.colorbar(contour, ax=self.ax)
        cbar.set_label(colorbar_label)
        return contour

    def show(self):
        plt.legend(frameon=False,fontsize=self.default_frontsize,loc='best')
        plt.tight_layout()
        plt.show()
        
    def save(self, filename):
        plt.legend(frameon=False,fontsize=self.default_frontsize,loc='best')
        plt.tight_layout()
        plt.savefig(filename, dpi=300)
        plt.close()
        

# 使用示例
if __name__ == "__main__":
    plot = AcademicPlot()
    plot.set_labels(title="Sample Plot", xlabel="X-axis", ylabel="Y-axis")
    plot.plot_line([2, 4, 6], [1, 4, 9], marker='x', markevery=2)
    plot.plot_scatter([2, 4, 6], [3, 5, 7])
    plot.plot_line([1, 2, 3], [1, 4, 9])  # 使用默认的线型、颜色和标记
    plot.plot_scatter([1, 2, 3], [2, 5, 8])  # 使用默认的散点样式和颜色
    plot.save("test.png")
