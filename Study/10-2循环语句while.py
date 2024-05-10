# @Time    : 2024/1/14 12:23
# @Author  : SU_SHAN_WAN_YU
# @File    : 10-2循环语句while.py
# @Description :
'''
产生随机数，可以猜多次，如果猜错
了给出提示，猜大了还是猜小了
如果一次猜对，打印……如果2-5次猜对，打印……
如果超过6次，打印……
'''
import random

count = 0
n = random.randint(1, 50)
print(n)
while True:
    m = int(input('请输入你猜的数：'))
    count += 1
    if n == m:
        if count == 1:
            print(f"恭喜你{count}次就猜对了，快去买彩票吧")
        elif 2 <= count <= 5:
            print(f"恭喜你{count}次猜对了，运气还行")
        elif count >= 6:
            print(f'恭喜你{count}次猜对了，运气有点差')
        break
    elif m > n:
        print('猜大了,再小一点')
    elif m < n:
        print('猜小了，再大一点')
