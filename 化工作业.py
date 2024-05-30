# @Time    : 2024/5/30 下午8:43
# @Author  : SU_SHAN_WAN_YU
# @FileName: 化工作业.py
# @Software: PyCharm
# @Description：化工作业

import numpy as np
import matplotlib.pyplot as plt


# 定义函数
def f(x):
    return 2 * x ** 2 + 6 * x + 7


# 定义函数的梯度
def df(x):
    return 4 * x + 6


# 梯度下降法
def gradient_descent(x_start, learning_rate=0.1, max_iter=100, tolerance=1e-6):
    x = x_start
    for i in range(max_iter):
        grad = df(x)
        if np.abs(grad) < tolerance:
            print(f"经过 {i} 次迭代后满足收敛条件。")
            break
        x -= learning_rate * grad
    return x


# 初始值
x_start = -5

# 使用梯度下降法
x_min = gradient_descent(x_start)
y_min = f(x_min)
print(f"最小值出现在 x={x_min:.2f}, y={y_min:.2f}")

# 让图片中可以显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 让图片中可以显示负号
plt.rcParams['axes.unicode_minus'] = False

# 绘制函数图像
x_range = np.linspace(-5, 5, 1000)
y_range = f(x_range)
plt.plot(x_range, y_range, label='函数f(x)')

# 绘制最小值点
plt.scatter(x_min, y_min, color='green', label='最小值点')

# 设置图例和标签为中文
plt.legend(labels=['函数f(x)', '最小值点'], loc='best')  # 使用labels参数指定图例标签
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('函数f(x) = 2x^2 + 6x + 7 及其最小值')

# 显示图像
plt.grid(True)
# plt.show()
plt.savefig('.\作业.png')
