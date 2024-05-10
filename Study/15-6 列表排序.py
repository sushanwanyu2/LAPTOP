# @Time    : 2024/1/22 10:23
# @Author  : SU_SHAN_WAN_YU
# @File    : 15-6 列表排序.py
# @Description :
'''
sort()默认是升序,通过reverse=True(升)/False(降)来控制为降序
reverse  单纯的一个反转.没有排序一说
'''

# 生成8-20之间的随机整数,保存到列表中,遍历打印

import random

numbers = []
for i in range(8):
    ran = random.randint(1, 100)
    numbers.append(ran)
print(numbers)  # 乱序列表

numbers.sort()
print(numbers)

numbers.sort(reverse=True)  # 降序排序
print(numbers)

numbers.reverse()  # 单纯地反转
print(numbers)

'''
生成8个1-20之间的随机整数,保存到列表中
键盘输入一个1-100之间的整数,将数量插入到排序后的列表中
'''
print('*' * 40)
num = []
for i in range(8):
    a = random.randint(1, 20)
    num.append(a)

b = int(input('请输入一个整数:'))
num.append(b)
num.sort()
print(num)
