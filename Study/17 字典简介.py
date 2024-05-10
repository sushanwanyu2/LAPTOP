# @Time    : 2024/1/25 9:48
# @Author  : SU_SHAN_WAN_YU
# @File    : 17 字典简介.py
# @Description :
'''
一.字典(dict)的概念:
Python字典是另一种可变容器模型,可存储任意类型对象。如字符串、数字、元组等其他容器模型

    因为字典是无序的所以不支持索引和切片。
二.字典(dict)的定义:
1.一般格式:
格式: 字典名={元素1,元素2,...}
元素以键值对存在==key(键值):value(实值)
2.空字典:
格式: 字典名={} 或者 字典名=dict()
注意:
key不可以重复,否则只会保留第一个;key不能修改,只能修改key后面的值
value值可以重复;
key可以是任意的数据类型,但不能出现可变的数据类型,保证key唯一;
key一般形式为字符串
3.添加元素
字典名[key]=value
4.修改元素
字典名[key]=value

二者公式一致,如果原字典中不存在该key,则是添加,否则是删除
'''
dict1 = {'name': '阿泽', 'age': 20, 'sex': '男'}
print(dict1)
dict2 = {}  # <class 'dict'>
dict3 = dict()  # <class 'dict'>
print(type(dict2), type(dict3))

dict1['name'] = '阿龙'  # 修改元素
print(dict1)
dict1['成绩'] = 90  # 添加元素
print(dict1)
# 改变年龄,键可以添加,删除,但是不能修改
dict1['age'] = 34
print(dict1)
'''
练习:
book={}
书名 价格 作者 出版社
促销:价格打折打八折
打印最终字典中的内容
'''
book = {}
book['name'] = '三体'
book['价格'] = 45
book['作者'] = '刘慈欣'
book['出版社'] = '科幻出版社'
print(book)
# 修改价格
book['价格'] *= 0.8
print(book)
