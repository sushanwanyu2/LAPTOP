# @Time    : 2024/5/9 19:33
# @Author  : SU_SHAN_WAN_YU
# @FileName: 作业1.py
# @Software: PyCharm
# @Description:作业1
# 导包
import numpy as np
import matplotlib.pyplot as plt

# 参数配置
# 让图片中可以显示中文
plt.rcParams['font.sans-serif'] = ('FangSong')

ci = 1
V0 = 1
F0 = 1
Fi1 = 5 * F0
Fi2 = 2 * F0
Fi3 = 1.00000001  # 由于Fi与F0不能相等，故使其二者有很小的差值。
t = np.linspace(0, 6, 1000)
c1 = ci - ci * V0 ** (Fi1 / (Fi1 - F0)) * ((Fi1 - F0) * t + V0) ** (-Fi1 / (Fi1 - F0))
c2 = ci - ci * V0 ** (Fi2 / (Fi2 - F0)) * ((Fi2 - F0) * t + V0) ** (-Fi2 / (Fi2 - F0))
c3 = ci - ci * V0 ** (Fi3 / (Fi3 - F0)) * ((Fi3 - F0) * t + V0) ** (-Fi3 / (Fi3 - F0))
# 调整细节
plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
plt.figure(figsize=(6, 4), dpi=300)  # 设置图像大小
plt.xlabel('时间T', size=12)
plt.ylabel('浓度c', size=12)
plt.xticks(fontproperties='Times New Roman', size=12)
plt.yticks(fontproperties='Times New Roman', size=12)
plt.xlim(0, 6.5)
plt.ylim(0, 1.0)
plt.title('搅拌器中浓度随时间的变化关系')
plt.text(0.9, 0.88, '①')
plt.text(1, 0.8, '②')
plt.text(1.1, 0.73, '③')
# 绘图
plt.plot(t, c1, ls='-.')
plt.plot(t, c2, ls='--')
plt.plot(t, c3)
# plt.show()
plt.savefig('.\崔玉超-2021110178.png')
