# @Time    : 2024/1/13 20:33
# @Author  : SU_SHAN_WAN_YU
# @File    : 10 循环语句while.py
# @Description :
'''
循环：
1.用户名和密码，反复输入
2.计算1-100之间的
3.游戏死亡重生
4.……
方式：
1.while
2.for

while格式：
while 条件：
    条件成立要循环执行的代码
'''
# # 打印1-10之间的数字
#
# # 初始值
# n = 1
# # 结束条件
# while n <= 10:
#     print(f'------>n={n}')
#     # 变量的变化使得程序可以执行完
#     n += 1
'''
1.打印1-50之间可以被3整除的数
2.打印1-10之间数字的累加和
'''
# # 1.
m = 1
while m <= 50:
    if m % 3 == 0:
        print(f'----->{m}')
    m += 1
# 2.
a = 1
total = 0  # 存放累计数据
while a <= 10:
    total += a
    a += 1
print(f'------->{total}')
