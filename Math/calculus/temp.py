import numpy as np
import matplotlib.pyplot as plt

# 1. 使用函数定义位置、速度和加速度 (更加通用和优雅)
def r(t): return np.array([t**2, np.exp(t), 2*t])
def v(t): return np.array([2*t, np.exp(t), 2])
def a(t): return np.array([2, np.exp(t), 0])

# 2. 生成数据 (为了图像比例更好，稍微缩小t的范围)
t_vals = np.linspace(-3, 3, 200)
x, y, z = r(t_vals)

# 3. 设置画布
fig = plt.figure(figsize=(10, 8)) # 增大画布尺寸
ax = fig.add_subplot(111, projection='3d')

# 4. 绘制主曲线
ax.plot(x, y, z, label='Trajectory', color='gray', alpha=0.6, linewidth=2)

# 5. 在特定点 t=1 绘制向量
t0 = 1
p0 = r(t0) # 起点坐标
v0 = v(t0) # 速度向量
a0 = a(t0) # 加速度向量

# 绘制质点当前位置
ax.scatter(*p0, color='black', s=50, label=f'Position at t={t0}')

# 绘制速度和加速度向量
# 使用 normalize=True 可以让箭头的视觉长度直接受 length 参数控制，避免被真实数值撑爆图表
ax.quiver(*p0, *v0, color='red', length=5, normalize=True, arrow_length_ratio=0.2, label='Velocity')
ax.quiver(*p0, *a0, color='blue', length=5, normalize=True, arrow_length_ratio=0.2, label='Acceleration')

# 6. 美化图表
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Kinematics: Velocity and Acceleration vectors')
ax.legend()

# 调整初始观察视角 (仰角和方位角)
ax.view_init(elev=20, azim=45) 

plt.show()