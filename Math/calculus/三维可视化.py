import numpy as np
import matplotlib.pyplot as plt
from skimage import measure

# 1. 定义三维空间的网格范围和精度 (切豆腐)
# 从 -1.5 到 1.5，切分 80x80x80 个网格。精度越高，曲面越平滑，但计算越慢
x_range = np.linspace(-1.5, 1.5, 80)
y_range = np.linspace(-1.5, 1.5, 80)
z_range = np.linspace(-1.5, 1.5, 80)

# 生成三维网格坐标矩阵
X, Y, Z = np.meshgrid(x_range, y_range, z_range, indexing='ij')

# 2. 将网格坐标代入你的非标准隐函数方程 f(x, y, z)
# 这里我们构造 F = f(x, y, z)，目标是寻找 F == 0 的面
F = (X**2 + (9/4)*Y**2 + Z**2 - 1)**3 - X**2 * Z**3 - (9/80)*Y**2 * Z**3

# 3. 使用 Marching Cubes 算法寻找 F=0 的等值面
# level=0.0 表示我们找的是 f(x,y,z) = 0 的表面
# 它会返回多边形的顶点 (verts) 和 面 (faces)
verts, faces, normals, values = measure.marching_cubes(F, level=0.0)

# 注意：算法返回的 verts 是网格的“索引编号”，我们需要把它还原为实际的 x, y, z 物理坐标
# 还原比例公式： 实际坐标 = 起点 + 索引 * 步长
x_step = (x_range[-1] - x_range[0]) / (len(x_range) - 1)
y_step = (y_range[-1] - y_range[0]) / (len(y_range) - 1)
z_step = (z_range[-1] - z_range[0]) / (len(z_range) - 1)

verts[:, 0] = x_range[0] + verts[:, 0] * x_step
verts[:, 1] = y_range[0] + verts[:, 1] * y_step
verts[:, 2] = z_range[0] + verts[:, 2] * z_step

# 4. 使用 matplotlib 的 plot_trisurf 绘制这些三角形网格
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 取出顶点的 X, Y, Z 坐标
x_verts = verts[:, 0]
y_verts = verts[:, 1]
z_verts = verts[:, 2]

# 绘制由三角形组成的曲面 (triangles 参数传入算法算好的 faces)
ax.plot_trisurf(x_verts, y_verts, z_verts, triangles=faces, 
                color='crimson', edgecolor='none', alpha=0.8)

# 5. 美化与视角调整
ax.set_title("Non-standard Implicit Surface: 3D Heart")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 保证长宽高比例一致，防止心形被拉伸
max_range = np.array([x_verts.max()-x_verts.min(), y_verts.max()-y_verts.min(), z_verts.max()-z_verts.min()]).max() / 2.0
mid_x = (x_verts.max()+x_verts.min()) * 0.5
mid_y = (y_verts.max()+y_verts.min()) * 0.5
mid_z = (z_verts.max()+z_verts.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()