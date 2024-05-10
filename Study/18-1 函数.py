# @Time    : 2024/1/28 12:12
# @Author  : SU_SHAN_WAN_YU
# @File    : 18-1 函数.py
# @Description :
'''
函数
    1.有参数
    2.无参数
无参数
def 函数名():
    pass
有参数
    def 函数名(参数1,参数2....):
        pass
参数的存在可以使定义的函数实现更多的功能login
'''
import random


def generate_code(n):
    # 生成验证码
    code = ''
    s = 'qwertyuQWERTYUIOPASDFGHJKLZXCVBNMiopasdfghjklzxcvbnm1234567890'
    for i in range(n):
        r = random.randint(0, len(s) - 1)
        code += s[r]
    print(code)


# 调用函数
generate_code(3)  # 借助参数n将外界的需求传入函数,使其可以实现确定的作用


# 登陆次数限制:m代表允许输入错误的次数
def login(m):
    count = 0
    while True:
        username = input('输入用户名:')
        password = input('输入登陆密码:')
        if username == 'admin' and password == '1234':
            print('登陆成功')
            break
        else:
            count += 1
            if count < m:
                print('用户名或密码错误,请重新输入')
            elif count >= m:
                print(f'{count}次无法成功登陆,账号已被锁定')
                break


login(3)
