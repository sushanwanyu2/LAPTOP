# @Time    : 2024/1/28 10:29
# @Author  : SU_SHAN_WAN_YU
# @File    : 17-9 列表推导式.py
# @Description :
'''
# 列表推导式:最终得到的是一个列表,得到列表的一种方式
格式:[i或者处理后的i,例如i+2 for i in 可迭代的]
'''
list1 = []
for i in range(1, 21):
    list1.append(i)
print(list1)

# 列表推导式,三句合并为一句话
list2 = [i for i in range(1, 21)]
print('list2=', list2)
list2 = [i + 2 for i in range(1, 10)]
print('list2=', list2)

# 将0-100之间所有的偶数,存放到列表中
list3 = [i for i in range(0, 101, 2)]
print(list3)

# list1 = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)
# 格式2: [i for i in 可迭代 if 条件]

list4 = [i for i in range(0, 101) if i % 2 == 0]
print(list4)
# 将字母打印出来
list2 = ['53', 'hello', '100', 'world', 'high', '88']
list5 = [i for i in list2 if i.isalpha()]  # 遍历list2放到list3中，判断是否是字母
print(list5)

# list2 如果h开头，首字母大写，不是h开头的全部转为大写
# 格式3:[结果1 if 条件 else 结果2 for 变量 in 可迭代]
list5 = [word.title() if word.isalpha() and word.startswith('h') else word.upper() for word in list2]
print(list5)

# new_list=[]
# for i in range(1,3):
#     for j in range(1,3):
#         new_list.append((i,j))
# print(new_list)

list6 = [(i, j) for i in range(1, 3) for j in range(1, 3)]
print(list6)

a = [x for x in range(1, 101)]
b = [a[i:i + 3] for i in range(0, len(a), 3)]
print(b)
