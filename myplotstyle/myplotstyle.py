import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, AutoMinorLocator
from itertools import cycle

# 设置字体和启用 LaTeX
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = True

class AcademicPlot(object):
    def __init__(self, ax=None, figsize=(8, 6), tick_count=5,default_frontsize = 20,theme='bright'):
        if ax is None:
            self.fig, self.ax = plt.subplots(figsize=figsize)
        else:
            self.fig = ax.get_figure()
            self.ax = ax
        self.default_frontsize = default_frontsize
        self.set_base_style(tick_count)
        self.set_theme(theme)
        self.default_markersize = 10
        self.default_markevery = 10
        

    def set_theme(self, theme):
        if theme == 'bright':
            sns.set_palette('bright')
        elif theme == 'muted':
            sns.set_palette('muted')
        elif theme == 'dark':
            sns.set_palette('dark')
        elif theme == 'deep':
            sns.set_palette('deep')
        
        self.colors = cycle(sns.color_palette())
        self.line_styles = cycle(['-', '--', '-.', ':'])
        self.markers = cycle(['o', 's', 'D', '^'])

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

    def plot_scatter(self, x, y, label=None, marker=None, color=None, is_filled=True, markersize=None):
        if marker is None:
            marker = next(self.markers)
        if color is None:
            color = "black"
        if markersize is None:
            markersize = self.default_markersize

        scatter_args = {
            'marker': marker,
            'color': color,
            'facecolor': color if is_filled else 'none',
            'label': label,
            's': markersize**2
        }

        self.ax.scatter(x, y, **scatter_args)


    def plot_line(self, x, y, label=None, linestyle=None, linewidth=2, color=None, marker=None, markevery=None, show_markers=False):
        if linestyle is None:
            linestyle = next(self.line_styles)
        if color is None:
            color = next(self.colors)
        if marker is None and show_markers:
            marker = next(self.markers)
        if markevery is None and show_markers:
            markevery = self.default_markevery

        plot_args = {
            'linestyle': linestyle,
            'linewidth': linewidth,
            'color': color,
            'label': label,
            'markersize': self.default_markersize
        }

        if show_markers:
            plot_args.update({
                'marker': marker,
                'markevery': markevery,
                'markerfacecolor': 'none',
                'markeredgewidth': 1,
                'markeredgecolor': color
            })

        self.ax.plot(x, y, **plot_args)


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
        self.fig.set_size_inches(8, 6)  # 设置图形的尺寸为8x6英寸
        plt.show()
        
    def save(self, filename):
        plt.legend(frameon=False,fontsize=self.default_frontsize,loc='best')
        plt.tight_layout()
        self.fig.set_size_inches(8, 6)  # 设置图形的尺寸为8x6英寸
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
        

# 使用示例
if __name__ == "__main__":
    plot = AcademicPlot()
    plot.set_labels(title="Sample Plot", xlabel="X-axis", ylabel="Y-axis")
    plot.plot_line([2, 4, 6], [1, 4, 9])
    plot.plot_scatter([2, 4, 6], [3, 5, 7])
    plot.plot_line([1, 2, 3], [1, 4, 9])  # 使用默认的线型、颜色和标记
    plot.plot_scatter([1, 2, 3], [2, 5, 8])  # 使用默认的散点样式和颜色
    plot.ax.set_xlim(0, 8)  # 设置 x 轴的范围
    plot.ax.set_ylim(0, 10)  # 设置 y 轴的范围
    plot.save("test.png")
