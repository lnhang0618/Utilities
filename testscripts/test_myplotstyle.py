from sciplotlib import AcademicPlot

# 使用示例
plot = AcademicPlot()
plot.set_labels(title="Sample Plot", xlabel="X-axis", ylabel="Y-axis")
plot.plot_line([2, 4, 6], [1, 4, 9], marker='x', markevery=2)
plot.plot_scatter([2, 4, 6], [3, 5, 7])
plot.plot_line([1, 2, 3], [1, 4, 9])  # 使用默认的线型、颜色和标记
plot.plot_scatter([1, 2, 3], [2, 5, 8])  # 使用默认的散点样式和颜色
plot.save("test.png")

