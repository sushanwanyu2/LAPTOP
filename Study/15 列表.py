# @Time    : 2024/1/19 11:21
# @Author  : SU_SHAN_WAN_YU
# @File    : 15 列表.py
# @Description :
'''
列表就是一个容器，可以来存储多个数据
超市的购物小票就是利用列表的例子
如何定义一个列表
1.空列表：[]
2.有内容的列表：【内容】，可以是字符串，可以是数字
可以带小数点

数据类型：int float str bool list，列表里面可以套
列表
即一个列表里面可以有各种数据类型
'''
list1 = []  # <class 'list'>
print(type(list1))
list2 = ['牛奶', '面包', '火腿肠', '辣条', '臭豆腐']

# 建立索引：0,1,2,3,4
# 获取列表里的元素,通过索引来获取对应元素
print(list2[3])
print(list2[0])
print(list2[-1])

# 切片操作
print(list2[:2])  # 包前不包后
print(list2[2:4])
print(list2[1::3])
print(list2[2::2])
print(list2[2:4])
print(list2[::-1])

