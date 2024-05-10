# @Time    : 2024/1/13 10:50
# @Author  : SU_SHAN_WAN_YU
# @File    : 9-1条件语句练习.py
# @Description :
import random

user_name = input('Enter your name:')
total = 1500  # 消费金额
money = 0  # 账户金额
coupon = 0  # 优惠券总金额
# 判断账户级别
if 0 < total < 500:  # lv1
    # 随机赠送3张1-10元优惠券
    # pass  # 起支撑结构作用
    coupon1 = random.randint(1, 10)
    coupon2 = random.randint(1, 10)
    coupon3 = random.randint(1, 10)
    # 将金额数加到coupon上
    coupon = coupon1 + coupon2 + coupon3
elif 500 <= total < 2000:
    # 随机赠送2张50元优惠券，若充值则送充值金额的10%
    coupon += 2 * 50
    # 嵌套if结构
    recharge = input(f'{user_name},请问是否要充值（送充值金额的10%）y/n')
    if recharge == 'y':
        money += 1.1 * int(input('请输入充值金额：'))
elif 2000 <= total:
    # 赠送2张100元优惠券，若若充值则送充值金额的15%
    coupon += 2 * 100
    recharge = input(f'{user_name}，请问是否要充值（送充值金额的15%）y/n')
    if recharge == 'y':
        money += 1.15 * int(input('请输入充值金额：'))
print('coupon', coupon, sep="=")
print('money', f'{money:.2f}', sep="=")
print('-----欢迎再次光临-----')
