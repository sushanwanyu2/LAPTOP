# @Time    : 2024/1/22 10:47
# @Author  : SU_SHAN_WAN_YU
# @File    : 15-7 列表的循环遍历.py
# @Description :


# 使用while循环
list0 = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条', '酸奶']
length = len(list0)
m = 0
while m <= length - 1:
    print(list0[m])
    m += 1

print('%' * 40)
# 使用for循环遍历打印
for i in range(length):
    print(list0[i])
for i in range(len(list0)):
    print(list[i])

for name in list0:
    print(name)  # 这种方式也可以

# python当中交换数值
a = 1
b = 2
a, b = b, a
print(a, b)  # 不用借助于第三个变量

a, b, c = b, a, b  # 从右往左看,b赋值给a,a赋值给b,b赋值给c
