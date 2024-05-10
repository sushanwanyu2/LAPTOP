# @Time    : 2024/1/16 10:22
# @Author  : SU_SHAN_WAN_YU
# @File    : 14 字符串.py
# @Description :


# 字符串
s1 = 'hello'
s2 = s1

s3 = 'hello'
s4 = 'hello1'
print(s1, s2, s3)
print(id(s1), id(s2), id(s3), id(s4))  # 查询字符串地址

# is  判断两个字符串地址是否一致
print(s1 is s2)
print(s2 is s4)

s1 = 'word'
print(s1, s2, s3)  # python当中有一个字符串大池子，里面有所有的字符串值

# 字符串 截取
s1 = 'ABCDEFG'  # 0-1-2-3-4-5-6 用index表示索引
# 或者最后一个为-1，-2 -3 -4 -5，依次类推
# 有两套索引机制
print(s1[6], s1[-1])
print(len(s1))  # 用len找字符串的长度
print(s1[0])