import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, AutoMinorLocator,ScalarFormatter
from itertools import cycle
import numpy as np
import matplotlib


# 设置字体和启用 LaTeX
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = True

class AcademicPlot(object):
    def __init__(self, ax=None, nrows=1, ncols=1,figsize=(8, 6), tick_count=5,fontsize = 17,theme='muted',show_minor_ticks=True):
        if ax is not None:
            self.fig = ax.figure
            self.ax = ax
        else:
            # 根据nrows和ncols创建子图
            self.fig, self.axs = plt.subplots(nrows, ncols, figsize=figsize,constrained_layout=True)

            # 如果只有一个子图，则将self.axs设置为单个轴对象
            if nrows == 1 and ncols == 1:
                self.ax = self.axs
            else:
                self.ax = None  # 在多子图情况下使用self.axs

        self.show_minor_ticks = show_minor_ticks
        self.figsize = figsize
        self.fontsize = fontsize
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

            ax.tick_params(axis='both', which='major', length=self.fontsize/3, width=self.fontsize/15, direction='in')
            ax.xaxis.set_major_locator(MaxNLocator(tick_count))
            ax.yaxis.set_major_locator(MaxNLocator(tick_count))

            for label in ax.get_xticklabels() + ax.get_yticklabels():
                label.set_fontsize(self.fontsize)

            if self.show_minor_ticks:
                ax.xaxis.set_minor_locator(AutoMinorLocator(tick_count))
                ax.yaxis.set_minor_locator(AutoMinorLocator(tick_count))
                ax.tick_params(axis='both', which='minor', length=self.fontsize/5, width=self.fontsize/30, direction='in')
            else:
                # 不显示副刻度
                ax.tick_params(axis='both', which='minor', length=0)

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
                
    def enable_scientific_notation(self,axis='both',ax=None):
        if ax is None:
            ax = self.ax

        if axis in ['y', 'both']:
            ax.ticklabel_format(style='sci', axis='y', scilimits=(-3, 4))
            ax.yaxis.offsetText.set_fontsize(self.fontsize)  # 调整y轴科学记数法标签的字体大小

        if axis in ['x', 'both']:
            ax.ticklabel_format(style='sci', axis='x', scilimits=(-3, 4))
            ax.xaxis.offsetText.set_fontsize(self.fontsize)  # 调整x轴科学记数法标签的字体大小

    def set_title(self, title,ax=None):
        if ax is None:
            ax = self.ax
        ax.set_title(title, fontsize=self.fontsize)
        
    def set_xlabel(self, xlabel,ax=None):
        if ax is None:
            ax = self.ax
        ax.set_xlabel(xlabel, fontsize=self.fontsize)

    def set_ylabel(self, ylabel,ax=None):
        if ax is None:
            ax = self.ax
        ax.set_ylabel(ylabel, fontsize=self.fontsize)

    def scatter(self, x, y, label=None, marker=None, color=None, is_filled=True, markersize=None,ax=None):
        if ax is None:
            ax = self.ax
            use_next = True
        else:
            use_next = ax == self.ax

        if marker is None and use_next:
            marker = next(self.markers)
        if color is None and use_next:
            color = "black"
        if markersize is None and use_next:
            markersize = self.default_markersize

        scatter_args = {
            'marker': marker,
            'color': color,
            'facecolor': color if is_filled else 'none',
            'label': label,
            's': markersize**2
        }

        ax.scatter(x, y, **scatter_args)


    def plot(self, x, y, label=None, linestyle=None, linewidth=2, color=None, marker=None, markevery=None, show_markers=False, ax=None):
        if ax is None:
            ax = self.ax
            use_next = True
        else:
            use_next = ax == self.ax

        if linestyle is None and use_next:
            linestyle = next(self.line_styles)
        if color is None and use_next:
            color = next(self.colors)
        if marker is None and show_markers and use_next:
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

        ax.plot(x, y, **plot_args)

    def contourf(self, X, Y, Z, cmap='jet', levels=100, colorbar_label=''):
        # 绘制等高线图
        contour = self.ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
        # 添加颜色条
        cbar = self.fig.colorbar(contour, ax=self.ax)
        cbar.set_label(colorbar_label)
        return contour

    def legend(self, ax=None, **kwargs):
        if ax is None:
            ax = self.ax
        ax.legend(fontsize=self.fontsize, **kwargs,frameon=False)


    def show(self):
        self.fig.set_size_inches(self.figsize[0], self.figsize[1])
        plt.show()
        
    def savefig(self, filename):
        self.fig.set_size_inches(self.figsize[0], self.figsize[1])
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
        

# 使用示例
if __name__ == "__main__":
    plot = AcademicPlot()
