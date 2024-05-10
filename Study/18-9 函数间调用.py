# @Time    : 2024/5/6 20:43
# @Author  : SU_SHAN_WAN_YU
# @FileName: 18-9 函数间调用.py
# @Software: PyCharm
# @Description
'''
def a():
    pass
def b():
    a()
'''


def a(flag):
    if flag:
        print('fat')
    else:
        print('sad')
    b()


def b():
    print('god')


# 通过调用a（），实现打印

a(True)
a(False)
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

