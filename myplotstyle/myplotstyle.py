import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, AutoMinorLocator
from itertools import cycle

# 设置字体和启用 LaTeX
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = True

class AcademicPlot(object):
    def __init__(self, ax=None, nrows=1, ncols=1,figsize=(8, 6), tick_count=5,fontsize = 20,theme='bright'):
        if ax is not None:
            self.fig = ax.figure
            self.ax = ax
        else:
            # 根据nrows和ncols创建子图
            self.fig, self.axs = plt.subplots(nrows, ncols, figsize=figsize)

            # 如果只有一个子图，则将self.axs设置为单个轴对象
            if nrows == 1 and ncols == 1:
                self.ax = self.axs
            else:
                self.ax = None  # 在多子图情况下使用self.axs
        
        self.default_fontsize = fontsize
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
        def apply_style(ax):
            ax.spines['top'].set_visible(True)
            ax.spines['right'].set_visible(True)
            ax.xaxis.set_major_locator(MaxNLocator(tick_count))
            ax.yaxis.set_major_locator(MaxNLocator(tick_count))

            ax.tick_params(axis='both', which='major', length=10, width=2, direction='in')
            ax.tick_params(axis='both', which='minor', length=5, width=1, direction='in')

            for label in ax.get_xticklabels() + ax.get_yticklabels():
                label.set_fontsize(self.default_fontsize)

            ax.xaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_minor_locator(AutoMinorLocator())

            for label in ax.xaxis.get_minorticklabels() + ax.yaxis.get_minorticklabels():
                label.set_visible(False)

        # 应用样式到单个ax或多个axs
        if self.ax is not None:
            apply_style(self.ax)
        else:
            for ax in self.axs.flat:
                apply_style(ax)


    ## 
    ##        functions
    ##

    def set_title(self, title):
        self.ax.set_title(title, fontsize=self.default_fontsize)
        
    def set_xlabel(self, xlabel):
        self.ax.set_xlabel(xlabel, fontsize=self.default_fontsize)

    def set_ylabel(self, ylabel):
        self.ax.set_ylabel(ylabel, fontsize=self.default_fontsize)

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
        plt.legend(frameon=False,fontsize=self.default_fontsize,loc='best')
        plt.tight_layout()
        self.fig.set_size_inches(8, 6)  # 设置图形的尺寸为8x6英寸
        plt.show()
        
    def savefig(self, filename):
        plt.legend(frameon=False,fontsize=self.default_fontsize,loc='best')
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
