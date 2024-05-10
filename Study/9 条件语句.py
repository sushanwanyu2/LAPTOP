# @Time    : 2024/1/12 14:20
# @Author  : SU_SHAN_WAN_YU
# @File    : 9 条件语句.py
# @Description :
'''
if……else……
if...elif...else
'''
# print(1)
# print(2)
# print(3)
#
# # 4、5有条件打印
# result = input('请输入（Y/N）')
# if result == 'Y':
#     print(4)
#     print('over~~~~~')
# print('-' * 20)
#
# # 随机数
# import random
#
# num = random.randint(1, 50)
# print(num)
# guess = input('请输入你猜的数：')
# if int(guess) == num:
#     print('恭喜你，猜对了!')
# else:
#     print('很遗憾,猜错了')
# # abs是一个内置函数，代表绝对值的意思
# # 多个条件下的if函数
# '''
# if 条件1：
#     条件1ture,执行
# elif 条件2：
#     条件2ture，执行
# ……
# else：
#     1、2……都不符合，执行
# '''
# # 输入销售金额，确定奖励金额
# '''
# 1-5:1000元
# 5-10：奖励笔记本
# 10-100：奖励iPhone12
# 超过100：奖励特斯拉
# 鼓励奖
# '''
# money = input('请输入销售金额：')
# if 10000 < int(money) <= 50000:
#     print('奖励1000元！恭喜！')
# elif 50000 < int(money) <= 100000:
#     print('奖励笔记本!恭喜！')
# elif 100000 < int(money) <= 1000000:
#     print('奖励iPhone12！恭喜！')
# elif int(money) > 1000000:
#     print('奖励特斯拉')
# else:
#     print('再接再励!毛绒玩具')
'''
人员管理系统：
功能：添加员工，删除员工，查询员工，更改信息
'''

print('-----------欢迎进入人员管理系统-----------')
choice = input('请选择功能：\n1.添加员工\n2.删除员工\n3.查询员工\n4.更改信息\n')
if choice == '1':
    print('添加员工')
elif choice == '2':
    print('删除员工')
elif choice == '3':
    print('查询员工')
elif choice == '4':
    print('更改信息')
else:
    print('输入错误，请重新输入')
print('-' * 40)
