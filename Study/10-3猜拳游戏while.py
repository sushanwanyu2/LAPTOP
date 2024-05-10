# @Time    : 2024/1/14 13:14
# @Author  : SU_SHAN_WAN_YU
# @File    : 10-3猜拳游戏while.py
# @Description :
'''
三局两胜猜拳游戏：
剪刀0，石头1，布2
可以有平局
'''
import random

person = 0
machine = 0
n = 1
while n <= 3:
    # 猜拳
    # 机器产生数字0,1,2
    ran1 = random.randint(0, 2)
    # 人猜数字
    guess = int(input('请输入剪刀0，石头1，布2：\n'))
    # 比较判断
    if (guess == 0 and ran1 == 2) or (guess == 1 and ran1 == 0) or (guess == 2 and ran1 == 1):
        print('~~~~~喜你，这一局你赢了~~~~~')
        person += 1
        n += 1
    elif (guess == 0 and ran1 == 1) or (guess == 1 and ran1 == 2) or (guess == 2 and ran1 == 0):
        print('~~~~~这一局机器赢了~~~~~')
        machine += 1
        n += 1
    elif (guess == 0 and ran1 == 0) or (guess == 1 and ran1 == 1) or (guess == 2 and ran1 == 2):
        print('~~~~~这一局平局~~~~~')
        person += 1
        machine += 1
        n += 1
    else:
        print('~~~~~输入错误，请重新输入~~~~~')
if person > machine:
    print(f'~~~~~恭喜，你以{person}:{machine}赢了机器~~~~~')
elif person == machine:
    print(f'~~~~~平局{person}:{machine}~~~~~')
elif person < machine:
    print(f'~~~~~机器以{person}:{machine}赢了你~~~~~')
