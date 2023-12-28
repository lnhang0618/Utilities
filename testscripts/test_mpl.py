import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset

# 创建一个简单的数据集用于绘图
x = range(0, 10)
y = [i**2 for i in x]

# 创建主图
fig, ax = plt.subplots()
ax.plot(x, y, label='Original Plot')

# 创建放大的子图，zoom参数是放大倍数，loc是放大框的位置
axins = zoomed_inset_axes(ax, zoom=2, loc=1)  # 可以调整zoom和loc来满足需求
axins.plot(x, y)

# 设置放大框的坐标轴范围
x1, x2, y1, y2 = 2, 4, 4, 16  # 这些值可以根据需要放大的区域进行调整
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

# 移除放大框的坐标轴刻度
axins.yaxis.set_visible(False)
axins.xaxis.set_visible(False)

# 画出放大区域的边框，并将其在原图上用矩形标记出来
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.savefig('test.png')
