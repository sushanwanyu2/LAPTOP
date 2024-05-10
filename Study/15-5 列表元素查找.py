# @Time    : 2024/1/22 9:27
# @Author  : SU_SHAN_WAN_YU
# @File    : 15-5 列表元素查找.py
# @Description :
'''
1.元素有没有在这个列表当中，用in    元素 in 列表
2.列表.index（元素），返回元素的下标位置，如果没有则报错(有处理方式)
3.列表.count(元素),返回整数
'''
list1 = [1, 2, 3, 4, 5, 6]
print(list1.count(2))  # 返回元素数量
print(list1.index(3))  # 返回下标位置
print(3.5 in list1)
print(3.4 not in list1)  # 返回bool值

print(id(list1))  # 查看内存位置
list2 = list1
list2.append(88)
print(id(list2))
print(list1)
print(list2)  # 此时list1和list2 相等,都加了88
# 二者内存地址一致,实际上list1和list2一模一样
del list2
print(list1)  # 实际不会报错,只是把和list1相同的list2删掉
# print(list2)



