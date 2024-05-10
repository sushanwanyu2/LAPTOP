# @Time    : 2024/1/28 11:37
# @Author  : SU_SHAN_WAN_YU
# @File    : 18 函数.py
# @Description :
'''
图书管理系统:
借书--->查询 书
还书--->查询 书
查询
只写一遍查询的内容
函数:复用

格式:
def 函数名([参数]可有可无):
    代码
函数名:get_name()
      search()

代码：
    封装重复内容
调用函数:
    函数名+()
'''
import random


def generate_code():
    # 生成验证码
    code = ''
    s = 'qwertyuQWERTYUIOPASDFGHJKLZXCVBNMiopasdfghjklzxcvbnm1234567890'
    for i in range(4):
        r = random.choice(s)
        code += r
    print(code)


print(generate_code)  # <function generate_code at 0x000001A55B1B0540>

# 验证函数是否可用?调用函数,后面加括号代表调用,否则代表查地址
generate_code()  # 调用函数,开始执行,函数中代码
'''
定义一个login函数:
admin 1234
输入一个用户名和密码,验证是否正确
'''


def login():
    username = input('输入用户名:')
    password = input('输入登陆密码:')
    if username == 'admin' and password == '1234':
        print('登陆成功')
    else:
        print('用户名或密码错误')


print(login)  # <function login at 0x0000014DF2E96C00>

login()  # 调用登陆函数
