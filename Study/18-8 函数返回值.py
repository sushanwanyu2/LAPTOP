# @Time    : 2024/5/6 20:13
# @Author  : SU_SHAN_WAN_YU
# @FileName: 18-8 函数返回值.py
# @Software: PyCharm
# @Description：函数返回值
'''
参数:外界向里面传值
返回值:里面的内容向外面传送
def 函数名（参数）：
    。。。
    。。。
    return XXX
当函数调用时通过return向外反出值
注意：1、当函数有返回值时，需要给一个变量承接
    2、return后面的值可以是一个，也可以是多个，
    如果是多个，将其打包成元组，再赋值给承接变量，
    作为整体返回。
'''


# def get_sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     # 将total返回
#     return total
#
#
# t = get_sum(1, 2, 3)  # 调用函数，将其放到元组当中打包。并将total调给t，借助于return关键字。
# x = 100
# x = x + t  # total变量外界想用用不了,此时需要用到返回值，将函数里面的调用出来。先调用，再用一个变量承接
# print(x)

def get_maxandmin(numbers):
    # 排序：冒泡排序
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print(numbers)
    # 获取头和尾
    min = numbers[0]
    max = numbers[-1]
    return min, max  # 先把两个值放到元组里面，再把元组送给变量
    # 返出


list1 = [34, 44, 12, 56, 36, 67, 78]
result = get_maxandmin(list1)
a, b = get_maxandmin(list1)  # 给a,b分开赋值,使得其不是元组.
print(a, b)
print(result)
