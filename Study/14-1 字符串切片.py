# @Time    : 2024/1/17 9:59
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-1 字符串切片.py
# @Description :
'''
字符串切片，列表也用
格式：字符串变量[start:end] 包前不包后
字符串变量[start:end:step] 默认是从左向右一个一个取值
step:两个作用，如果从左往右取值，step为一个正数，step是一个负数，
则代表从右向左取值
'''
s = 'ABCDEFG'
print(s[0:5])
print(s[1:4])
print(s[4:])  # 从4到尾
print(s[:5])  # 头和尾都可以省略
print('*' * 40)
print(id(s[:]))
print(id(s))  # 字符串值一样，地址则一样
# 取中间不要两头
print(s[1:6])
print(s[1:-1])

print(s[:-1:2])  # 拿到ACE
print(s[1:-1:2])  # 拿到BDF
print(s[::4])
print('&'*30)
print(s[::-1])
print(s[-3::-4])  # step规定的顺序必须和start以及end的顺序一致
# print(s[0:6:-2]) 拿不到任何值必须
print(s[6::-2])
