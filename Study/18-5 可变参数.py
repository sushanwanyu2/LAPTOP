# @Time    : 2024/1/30 11:43
# @Author  : SU_SHAN_WAN_YU
# @File    : 18-5 可变参数.py
# @Description :
'''
可变参数:
*args
*kwargs

拆包和装包
函数装包：
def 函数（*args）：------>此时会出现装包
    pass
函数(1,2,3,4)

拆包:
list tuple set
调用的时候"
函数(*list)|函数(*tuple)|函数(*set)
拆包过程
'''


# 求和
# def get_sum(a, b):
#     r = a + b
#     print(r)
#
#
# get_sum(2, 3)


def get_sum(*args):  # *号必须要在，代表一个容器，是一个元组
    # print(args)  # (1, 2, 3, 4)
    s = 0
    for i in args:
        s += i
    print('和:', s)


get_sum(1, 2, 3, 4)

a, *b, c = 1, 2, 3, 4, 5
print(a, b, c, sep='*')  # 1*[2, 3, 4]*5

a, b, c = (1, 2, 3)  # 1*2*3
print(a, b, c, sep='*')

a, *b, c = (1, 2, 3, 4)
print(a, b, c, sep='*')  # 1*[2, 3]*4

# 求随机数列表的和
ran_list = [23, 44, 5, 634, 674, 56]

get_sum(*ran_list)  # 调用的时候加*是拆包
