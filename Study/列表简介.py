# @Time    : 2023/10/13 22:07
# @Author  : SU_SHAN_WAN_YU
# @File    : 列表简介.py
# @Description :列表学习
# 在Python当中，[]代表列表，举例如下
bicycles = ['trek', 'cannondale', 'redline', 'speclized']
print(bicycles)
# 打印的内容为整个列表
# 若想访问特定列表，则如下所示
print(bicycles[0])
print(bicycles[1])
print(bicycles[-1])
# 开头从0开始，末尾可以是-1
# 如何修改，添加，删除元素
bicycles[0] = 'red'  # 将第一个元素修给为red
print(bicycles)
print("-*" * 15)
bicycles.append('red1')  # 用.append在最后添加元素red
print(bicycles, '\n', '-*' * 15, sep='')
bicycles.insert(0, 'red2')  # 在0的位置插入一个新的元素
print(bicycles)

del bicycles[0]  # 删除第一个元素
print(bicycles)
# such as
del bicycles[2]  # 删除第三个元素
print(bicycles)
'''
使用pop（）方法删除删除列表最后的元素，并且这个元素可以被接着使用，
将其赋给另一个变量,括号当中加上确切的位置坐标则可以删除特定值
del可以定义删除某一个特定的元素
'''
bicycle = bicycles.pop()  # 删除最后一个元素并将其储存在bicycle当中
print('\n', bicycles)
print('\n', '被删除的元素：', bicycle)
print('\n', bicycles)

'''
当不确定所要移除的元素所在的位置时，可以
使用.remove（）来移除
'''
bicycles.remove('red')
print('\n', bicycles)

# 使用sort()对列表进行永久性排序
cars = ['audi', 'bmw', 'subaru', 'toyota']
cars.sort()  # 修改后再也无法恢复原来的排列顺序
print('\n', cars)
cars1 = ['audi', 'bmw', 'subaru', 'toyota']
cars1.sort(reverse=True)  # 按照字母的反序进行排序
print('\n', cars1)

# 使用sorted（）对列表进行临时性排序
# 函数sorted可以保持列表元素的原始排列顺序，同时按照特定的顺序显示该列表
cars2 = ['audi', 'bmw', 'subaru', 'toyota']
print('\n', 'Here is the original list:')
print(cars2)
print('\nHere is the sorted list:')
print(sorted(cars2))
print('\nHere is the original list:')
print(cars2)
print('\n', 'Here is the sorted1 list:', sorted(cars2, reverse=True))  # 增加传递函数reverse=Ture，使得排序按照字母的反序
