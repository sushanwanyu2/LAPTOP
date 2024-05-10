# @Time    : 2024/5/1 13:01
# @Author  : SU_SHAN_WAN_YU
# @FileName: 绘制折线图.py
# @Software: PyCharm
# @Description: 折线图
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, linewidth=3)
plt.title('practice', fontsize=18)
plt.xlabel('history', fontsize=18)
plt.ylabel('study', fontsize=18)
plt.show()
