# @Time    : 2024/1/24 11:50
# @Author  : SU_SHAN_WAN_YU
# @File    : 16 元组.py
# @Description :
'''
元组与列表类似:
1.元组的元素不能修改
2.元组使用圆括号(),列表使用方括号[]
list 列表
tuple 元组
定义:
名=()
注意事项:
如果元组中只有一个元素,必须添加逗号('aaa',)
相互转换:
    list(tuple) 表示元组转列表
    tuple(list) 列表转元组
方法:
    count()
    index()
关键字:
    in, not in
    for....in
    while
'''
t1 = ()
print(type(t1))  # <class 'tuple'>

t2 = ('aa')
print(type(t2))  # <class 'str'>

t3 = ('aa',)
print(type(t3))  # <class 'tuple'>,逗号是关键

t4 = ('a', 'b', 'c', 'a')
print(type(t4))

# 下标和切片同样适用 下标不要越界
print(t4[2])

print(t4[::-1])
print(t4.count('a'))
print(t4.index('a', 1))
# in print for i in t4: 等也可以用

for i in t4:
    print(i)
# 如果非要改，则可以转换格式,但会浪费内存
# list(tuple) 表示元组转列表
# tuple(list) 列表转元组

print(list(t4))  # ['a', 'b', 'c', 'a']
