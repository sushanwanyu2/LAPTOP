# @Time    : 2024/5/6 20:59
# @Author  : SU_SHAN_WAN_YU
# @FileName: 18-10 全局变量和局部变量.py
# @Software: PyCharm
# @Description

'''
验证是否登录：islogin：
自定义一个判断用户是否登录成功的islogin
参数：username，password
函数体：
判读输入的用户名和密码是否正确，返回True或者False
借书：borrow_book
参数：书名
函数体：判断是否登录，若没有登录，提示还未登录，不能借书
'''

is_login = False


def login(username, password):
    if username == 'admin' and password == '1234':
        print('登陆成功')
        is_login = True
    else:
        print('login is false')
        return False


def borrow_book(book_name):
    if is_login:
        print(f'成功借阅{book_name}')
    else:
        print('还未登陆，无法借书!')
        username = input('用户名：')
        password = input('<PASSWORD>')
        login(username, password)


# 为啥无法借书，即全局变量和局部变量的问题
'''
全局和局部变量：
局部变量作用范围仅限于函数内部
'''
a = 100  # 全局变量


def test1():
    a = 0  # 局部变量
    b = 20
    print('a=', a)


def test2():
    # 局部变量作用范围仅限于函数内部
    print('a=', a)  # 引用出全局变量的值
    # print('b=', b)


def test3():
    # 想要改变全局a的值,首先要找到a的值
    # a-=10  #没有权限调用
    print('a=', a)


test1()

test2()
