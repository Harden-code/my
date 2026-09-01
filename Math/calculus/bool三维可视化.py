import numpy as np
import matplotlib.pyplot as plt

# 1. 生成高密度的三维网格
# 注意：散点图需要更高的网格密度才能看出形状，这里设为 100
x = np.linspace(-1.5, 1.5, 100)
y = np.linspace(-1.5, 1.5, 100)
z = np.linspace(-1.5, 1.5, 100)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# 2. 计算隐函数 F(x, y, z)
F = (X**2 + (9/4)*Y**2 + Z**2 - 1)**3 - X**2 * Z**3 - (9/80)*Y**2 * Z**3

# 3. 核心：NumPy 布尔过滤
# 因为是离散网格，F 极大概率不会“刚好”等于 0
# 所以我们需要设定一个容差 epsilon，寻找绝对值小于 epsilon 的点
epsilon = 0.01 
mask = np.abs(F) < epsilon  # 得到一个三维的布尔数组
print(mask)
# 使用 mask 过滤出所有符合条件的 X, Y, Z 坐标
x_pts = X[mask]
y_pts = Y[mask]
z_pts = Z[mask]

# 4. 使用散点图 (scatter) 绘制点云
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# s=1 表示散点的大小，alpha=0.3 增加透明度让点云看起来更柔和
ax.scatter(x_pts, y_pts, z_pts, c='crimson', s=1, alpha=0.3, marker='.')

ax.set_title("Point Cloud Surface using NumPy Boolean Filter")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 保持长宽高比例一致
max_range = np.array([x_pts.max()-x_pts.min(), y_pts.max()-y_pts.min(), z_pts.max()-z_pts.min()]).max() / 2.0
mid_x = (x_pts.max()+x_pts.min()) * 0.5
mid_y = (y_pts.max()+y_pts.min()) * 0.5
mid_z = (z_pts.max()+z_pts.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()