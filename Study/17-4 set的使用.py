# @Time    : 2024/1/26 9:49
# @Author  : SU_SHAN_WAN_YU
# @File    : 17-4 set的使用.py
# @Description :
'''
集合:
set
特点:没有重复,无序的(没有下标)
花括号里面不是键值对的时候就是集合
add添加元素
'''
import random

set1 = {'张三'}  # 花括号里面不是键值对的时候就是集合
print(type(set1))

#
list1 = [1, 3, 6, 8, 9, 9, 1, 2, 3, 4, ]

list1 = list(set(list1))
print(list1)  # 列表去除重复元素,直接转换为集合再强转为list

set3 = set()  # 声明空集合
print(type(set3))

set3.add('流量地球')
print(set3)
set3.add('盗墓笔记')
print(set3)  # add添加元素

# append  extend  insert----->list
# add      update ----->set
# list:有序,允许重复
# set: 无序,不允许重复

set1.update(set3)
print(set1)  # 合并集合
result = set3.add('西游记')
print(set3)  # 第二本重名的加不进来
print(result)  # 没有返回值
'''
产生5组(不允许重复),字母和数字组成的四位验证码
最终打印5组验证码
'''
import random

code_list = set()
s = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
while True:
    # 判断长度
    if len(code_list) == 5:
        break
    code = ''
    for i in range(4):
        # r = random.choice(s)
        # code += r
        index = random.randint(0, len(s) - 1)
        code += s[index]
    # 将code添加到list中
    code_list.add(code)
print(code_list)
# 如果重复在集合当中是添加不进去的