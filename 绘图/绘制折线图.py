# @Time    : 2024/5/8 20:38
# @Author  : SU_SHAN_WAN_YU
# @FileName: 绘制折线图.py
# @Software: PyCharm
# @Description:绘制折线图
from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
# 设置图片大小
fig = plt.figure(figsize=(20, 10), dpi=300)
# 设置x的刻度
# plt.xticks(x)
plt.xticks(range(2, 26, 2))
plt.yticks(range(min(y), max(y) + 1))
# 绘图
plt.plot(x, y)
# 保存图片
# plt.savefig('')
# 展示
plt.show()
