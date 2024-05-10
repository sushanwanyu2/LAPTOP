# @Time    : 2024/1/30 9:59
# @Author  : SU_SHAN_WAN_YU
# @File    : 18-2 带多个参数的函数.py
# @Description :
'''
带多个参数的函数:
def 函数名(参数1,参数 2,...):
    函数体
# isinstance(变量,类型)用来判断a是否是某类型
1.定义函数
2.调用函数
'''


# 判断是否是整形
# def get_sum(a, b):
#     if isinstance(a, int) and isinstance(b, int):  # isinstance(变量,类型)用来判断a是否是某类型
#
#         s = a + b
#         print(s)
#     else:
#         print('类型错误')
#
#
# get_sum(1, 2)
# get_sum('hello', ' world')


# 判断用户是否登陆

def is_login(username, password, is_remember=False):  # 最后的这个参数称为默认值参数
    # 函数体起验证功能
    print('是否记住密码', is_remember)
    if username == 'admin' and password == '1234':
        print('登陆成功')
    else:
        print('登陆失败')


is_login('admin', '1234')
