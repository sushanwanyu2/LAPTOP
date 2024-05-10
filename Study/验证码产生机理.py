# @Time    : 2024/1/17 13:02
# @Author  : SU_SHAN_WAN_YU
# @File    : 验证码产生机理.py
# @Description :验证码产生机理
import random

# word = ''
# s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
# for i in range(6):
#     m = random.randint(0, len(s) - 1)
#     word = word + s[m]
# print(word, end='')
time=('')
s='qwertyuiopasdfghjklzxcvbnm1234567890'
for i in range(6):
    a=random.randint(0,len(s)-1)
    time+=s[a]
print(time)
