# @Time    : 2024/1/15 12:21
# @Author  : SU_SHAN_WAN_YU
# @File    : 13 循环的嵌套.py
# @Description :
'''
if 条件：
    if 条件：
        pass
else：
    if 条件：
        pass

while循环
****
****
****
****

*
**
***
****
*****
'''

n = 1
while n <= 4:
    print('*' * 4)
    n += 1
print('-' * 30)
n = 1
while n <= 5:
    print('*' * n)
    n += 1
print('-' * 30)
n = 1
while n <= 5:  # 5控制行数
    m = 0
    while m < n:
        print('*', end='')
        m += 1
    n += 1
    print()
'''
*****
****
***
**
*
'''
print('-' * 30)
m = 5
while m >= 1:
    print('*' * m)
    m -= 1
'''
for 循环打印图像
*
**
***
****
*****
'''
for i in range(5, 0):
    print('*' * i)
