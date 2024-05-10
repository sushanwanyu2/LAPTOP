# @Time    : 2024/1/21 11:44
# @Author  : SU_SHAN_WAN_YU
# @File    : 15-3重复元素的删除.py
# @Description :

#------------------------------------------------------------------
# for循环解决方案
list0 = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条', '酸奶']

result_list = []
for i in list0:
    if i != '酸奶':
        result_list.append(i)
list0 = result_list
print(list0)
# ------------------------------------------------------------------
list2 = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条', '酸奶']
for i in range(list2.count('酸奶')): 
    list2.remove('酸奶')
print(list2)
# ------------------------------------------------------------------
# while循环解决方案
list1 = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条', '酸奶']
n = 0
while n <= len(list1) - 1:
    if list1[n] == '酸奶':
        list1.remove('酸奶')
    else:
        n += 1
print(list1)
