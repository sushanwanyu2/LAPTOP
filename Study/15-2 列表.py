# @Time    : 2024/1/21 10:39
# @Author  : SU_SHAN_WAN_YU
# @File    : 15-2 列表.py
# @Description :
'''
pop（index）：根据下标删除元素，下标注意不要超出范围index out of range
pop()：表示从后往前依次删除
remove（value）：根据元素名称进行删除，若删除的元素列表中不存在，则x not in list
只删除遇到的第一个元素，后面的元素不会被删除,全部删则需要用到循环
clear：清空列表元素
关键字in：元素是否在列表中？返回值是一个bool类型
'''
list1 = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条', '酸奶']
# # list1.pop(-1)
# # print(list1)
#
# # remove
# list1.remove('辣条')
# print(list1)
#
# # 删之前先判断是否存在这个元素,用到了关键字in
# if '辣条啊' in list1:
#     print('存在')
# else:
#     print('不存在')

# for i in list1:
#     if i == '酸奶':
#         list1.remove(i)
# print(list1)  # 有紧挨着的会发送漏删的情况，由于删除完之后列表的角标index会发生变化
#                 # 故会发生漏删的发生
# 用while循环解决漏删问题
# n = 0
# while n <= len(list1)-1:
#     if list1[n] == '酸奶':
#         list1.remove('酸奶')
#     else:
#         n += 1
# print(list1)

# for循环解决方案
list0 = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条', '酸奶']
elem = 1
result_list = []
for i in list0:
    if i != '酸奶':
        result_list.append(i)
list0 = result_list
print(list0)

list1.clear()
print(list1)