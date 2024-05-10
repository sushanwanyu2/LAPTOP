# @Time    : 2024/1/21 12:00
# @Author  : SU_SHAN_WAN_YU
# @File    : 15-4列表元素修改.py
# @Description :
'''
修改：
[1,2,3,4,5,6]
insert（index，object），在某一个位置插队，占用指定的位置
其它元素向后移动
index根据元素找该元素的位置，返回值指的是下标位置

del:删除某一个元素,del 列表()或者del list--->删除全部列表(包括变量)
'''
list1 = [1, 2, 3, 4, 5, 6]
list1.insert(1, 8)  # insert表示插队，而不是完整的修改
print(list1)

location = list1.index(4)  # index根据元素找该元素的位置
list1[location] = 7
print(list1)

# del list1 [3] 和list.pop[3]效果相同

list1.clear()
list1.append(1000)

del list1
print(list1)  # list1 会被del全部删除,该变量也被删除
