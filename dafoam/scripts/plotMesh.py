import pyvista as pv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# 假设我们想在y=0处绘制网格
z_value = 0.0


def sort_points_clockwise(points, center):
    # 计算每个顶点相对于中心的角度
    angles = np.arctan2(points[:, 1] - center[1], points[:, 0] - center[0])
    # 根据角度排序顶点
    return points[np.argsort(angles)]


# 读取 VTK 文件
mesh = pv.read('/home/dafoamuser/workspace/tutorials/2dflat/gammaSSTFieldInversion_CgInit/VTK/gammaSSTFieldInversion_CgInit_0/internal.vtu')

# 获取点坐标
points = mesh.points

# 获取单元格信息
cell_points_ids = mesh.cells.reshape(-1, 9)[:, 1:9]


# 创建一个 Matplotlib 图表
fig, ax = plt.subplots()

# 遍历每个单元格
for cell_id in cell_points_ids:
    # 获取单元格的顶点
    cell_points = points[cell_id]
    
    # 筛选出 z=0 的顶点
    cell_points_at_z = cell_points[cell_points[:, 2] == z_value]

    # 如果这个单元格在z=0平面上没有四个顶点，跳过
    if cell_points_at_z.shape[0] != 4:
        continue

    # 计算这四个点在xy平面的中心
    center = cell_points_at_z.mean(axis=0)

    # 对这些点进行排序，以确保它们按顺时针或逆时针方向连接
    sorted_points = sort_points_clockwise(cell_points_at_z[:, [0, 1]], center[[0, 1]])

    # 将最后一个点连接到第一个点，闭合四边形
    sorted_points = np.vstack([sorted_points, sorted_points[0]])

    # 绘制四边形的边界
    ax.plot(sorted_points[:, 0], sorted_points[:, 1], color='black', linewidth=0.5)


ax.annotate('U_in', xy=(0, 0.1), xytext=(-0.2, 0.1),
            arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1),
            clip_on=False,
            fontsize='large', fontweight='bold', color='blue',
            va='center', ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', edgecolor='none', alpha=0.5))

'''
# 绘制复杂的图形元素，例如曲线
pressure_side = patches.Arc((0.5, 0), 0.2, 0.4, angle=0, theta1=0, theta2=180, edgecolor='red')
ax.add_patch(pressure_side)

# 绘制颜色和样式自定义的线
ax.plot([1, 2], [1, 2], color='blue', linestyle='--', linewidth=2)
'''


# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('y')  # 在 xy 平面上

ax.set_xlim(left=-0.1)
ax.set_ylim(bottom=0)


# 显示图表
plt.show()