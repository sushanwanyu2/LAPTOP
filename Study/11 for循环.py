# @Time    : 2024/1/15 9:54
# @Author  : SU_SHAN_WAN_YU
# @File    : 11 for循环.py
# @Description :
'''
格式：
for 变量名 in range(n)：
    循环体中的内容


range(n)  表示从0开始取值，在n-1截止
    range(stop) -> range object
    range(start, stop[, step]) -> range object 包前不包后[start, stop)
    step表示步长
'''

# 1-10 数字打印

for i in range(1, 11):  # 默认从0开始，不包括后面的值
    print(i)
print('&' * 40)
for i in range(5, 50, 2):
    print('----->', i)

sum = 0
for i in range(1, 51):
    sum += i
print(sum)

# 最多输入三次账号与密码，否则提示账号被锁定
# break退出循环

print('&' * 40)
for i in range(3):
    # 提示输入用户名和密码
    username = input('输入用户名：')
    password = input('输入密码：')
    if username == 'admin' and password == '1234':
        print('登陆成功')
        break
    print('用户名或密码有误')
if i == 2:
    print('账户被锁定')
