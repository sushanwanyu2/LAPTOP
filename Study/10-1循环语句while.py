# @Time    : 2024/1/14 10:55
# @Author  : SU_SHAN_WAN_YU
# @File    : 10-1循环语句while.py
# @Description :
'''
去超市买东西结算总额，输入价格和数量，
允许买多件商品
'''

# count = 0
# while True:
#     print('11111')
#     count += 1
#     if count == 5:
#         break  # 跳出当前的循环结构



total = 0
nums = 0
while True:
    # 先买后问
    price = float(input('价格'))
    number = int(input('数量'))
    # 完成累加
    nums += number
    total += price * number
    # 判断是否继续购买
    print('当前商品总额是{:.2f}'.format(total))
    answer = input('是否继续添加商品（e表示退出，其余字母继续添加）？')
    if answer == 'e':
        break
print('当前共{}件商品，总额是{:.2f}'.format(nums, total))
