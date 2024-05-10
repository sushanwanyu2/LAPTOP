# @Time    : 2024/1/26 11:03
# @Author  : SU_SHAN_WAN_YU
# @File    : 17-5 集合移除.py
# @Description :
set1 = {'RLI3', 'IW74', 'WKny', 'rpDf', '8Ood'}
set1.remove('8Ood')  # 如果不存在会报错
print(set1)

set1.discard('8Ood')
print(set1)
set1.discard('8ood')
print(set1)  # 不存在,不删掉也不会报错

# del 实现删除
# del set1
# set1.clear()  # 清空内容
set1.pop()  # 随机进行删除
print(set1)

# 集合:交集intersection,并集union,差集difference
set2 = {1, 2, 3, 4, 5}
set3 = {3, 4, 5, 6, 7, 8, 9}
result = set2.intersection(set3)
print(result)

result = set2.union(set3)  # | 并集 &交集
print(result)
result = set3.difference(set2)
print(result)

print(set2&set3)
print(set2|set3)
print(set2-set3)  # 差集

'''
list:允许重复,有序,有下标[]
tuple:允许重复,里面的元素不能增删改,只能查看()
dict:键值对存在,  键:唯一,值:允许重复{}
set:不允许重复,无序{}
'''
'''
类型转换问题:
list---->tuple,set(长度可能发生改变)
tuple---->list,set
set---->list,tuple
dict---->list,tuple,set 只是将字典的键放到列表里面
'''