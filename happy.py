import numpy as np
import matplotlib.pyplot as plt

# 尝试修改这些数字，会有惊喜
n = 1000
k = 6  # 改变这个数字试试 2, 3, 4, 7...
theta = np.linspace(0, 2*np.pi, n)
r = np.cos(k * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(6,6))
plt.plot(x, y, color='purple')
plt.title(f"Spirograph k={k}")
plt.axis('off') # 关掉坐标轴，只看艺术图
plt.show()