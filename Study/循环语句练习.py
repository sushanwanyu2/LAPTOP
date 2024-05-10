# @Time    : 2024/1/15 18:04
# @Author  : SU_SHAN_WAN_YU
# @File    : 循环语句练习.py
# @Description :
'''
掷骰子
两个：1-6
1.玩游戏要有金币，没金币不能玩__
2.玩游戏赠送金币（1枚），充值获取金币__
3.10元的倍数充值，10元20个金币__
4.玩游戏消耗金币，一局5个金币__
5.猜大小：猜对有奖励金币（2枚），猜错没有奖励。总数超出6点以上为大，否则为小__
6.游戏结束 1）主动退出 2）没金币退出__
7.退出打印剩余金币数，共完了几局__
'''
import random

count = 0
coins = 0
if coins < 5:
    while True:
        money = int(input('余额不足，请输入充值金额（元）：'))
        if money % 10 == 0:
            coins = coins + money // 10 * 20
            print(f'充值成功，当前金币余额为{coins}个')
            print('~~~~~欢迎登陆游戏~~~~~')
            answer = input('是否想要开始游戏（y/n）：')
            while answer == 'y' and coins >= 5:
                ran1 = random.randint(1, 6)
                ran2 = random.randint(1, 6)
                # print(ran1, ran2)
                coins -= 5
                coins += 1
                count += 1
                guess = input('已完成洗牌，请猜大小：')
                if guess == '大' and ran1 + ran2 > 6 or guess == '小' and ran1 + ran2 <= 6:
                    print('恭喜，你赢了！')
                    coins += 2
                else:
                    print("很遗憾，你输了！")
                answer = input('是否想要继续游戏（y/n）：')
            else:
                print('金币余额不足，将自动结束游戏')
            print(f"共玩了{count}局，剩余金币数为{coins}个")
            break
        else:
            print('充值金额必须是10的倍数，请重新输入充值金额')
            a = input('按任意键继续充值，q直接退出：')
            if a == 'q':
                break
