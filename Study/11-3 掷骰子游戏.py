# @Time    : 2024/1/15 10:50
# @Author  : SU_SHAN_WAN_YU
# @File    : 11-3 掷骰子游戏.py
# @Description :
'''
掷骰子
两个：1-6
1.玩游戏要有金币，没金币不能玩
2.玩游戏赠送金币（1枚），充值获取金币
3.10元的倍数充值，10元20个金币
4.玩游戏消耗金币，一局5个金币
5.猜大小：猜对有奖励金币（2枚），猜错没有奖励。总数超出6点以上为大，否则为小
6.游戏结束 1）主动退出 2）没金币退出
7.退出打印剩余金币数，共完了几局
'''

import random

# 计数器
count = 0
# 金币数
coins = 0
if coins < 5:
    # 提示充值
    print('金币不足，请充值')
    while True:  # 多次充值
        money = int(input('请输入充值金额:'))
        # 10元的倍数充值，
        if money % 10 == 0:
            coins += money // 10 * 20
            print(f'充值成功！当前金币数为{coins}个')
            # 开启游戏之旅
            print('~~~~~~~开启游戏之旅~~~~~~~')
            answer = input('是否开始游戏（y/n）:')
            while coins > 5 and answer == 'y':
                # 先去扣金币
                coins -= 5
                # 赠送金币
                coins += 1
                # 产生两枚随机的骰子数
                ran1 = random.randint(1, 6)
                ran2 = random.randint(1, 6)

                while True:
                    # 猜大小
                    guess = input('洗牌完毕，请猜大小：')
                    # 判断比较
                    if guess == '大' and ran1 + ran2 > 6 or guess == '小' and ran1 + ran2 <= 6:
                        print('恭喜，你赢了！')
                        coins += 2
                        break
                    elif guess == '大' and ran1 + ran2 <= 6 or guess == '小' and ran1 + ran2 > 6:
                        print('很遗憾，本次猜错了')
                        break
                    else:
                        print("输入错误，请重新输入")
                # 玩的次数
                count += 1
                answer = input('是否继续游戏(Y/N)')
            # 打印玩的次数和剩余金币数
            print(f'共完了{count}次，剩余{coins}枚金币')
            break

        else:
            print('不是10的倍数，充值失败')
