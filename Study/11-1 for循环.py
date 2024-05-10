 # @Time    : 2024/1/15 10:29
# @Author  : SU_SHAN_WAN_YU
# @File    : 11-1 for循环.py
# @Description :
'''
for...else...
for i in range():
    循环体
else:
    如果上面的for循环0-n-1没有出现中断（break）
'''

for i in range(3):
    # 提示输入用户名和密码
    username = input('输入用户名：')
    password = input('输入密码：')
    if username == 'admin' and password == '1234':
        print('登陆成功')
        break
    print('用户名或密码有误')
else:
    print('账户被锁定！')

# while...else...
n = 1
while n <= 10:
    print(n)
    n += 1
else:  # 不被中断才会执行
    print('over')

n = 1
while n <= 10:
    print(n)
    if n == 5:
        break
    n += 1
else:  # 不被中断才会执行
    print('over')
