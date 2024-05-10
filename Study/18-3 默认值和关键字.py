# @Time    : 2024/1/30 10:18
# @Author  : SU_SHAN_WAN_YU
# @File    : 18-3 默认值和关键字.py
# @Description :
'''
默认值参数:在定义函数的时候有一个或者多个参数已经被赋值
        必须在最后的位置
def 函数名(参数1,参数2,参数3=值,参数4=值,参数5=值):
    pass
调用特点:
函数名(值1,值2)
注意:
在定义函数的时候,普通函数得位于默认值的前面,默认值位于最后

关键字参数:调用函数的时候明确指定,使用关键字参数赋值,
默认参数的顺序是固定的
'''


def book_name(bookname, user_name, number=1, school='二小'):
    print(f'进入{school}借书系统...')
    print(f'{user_name}要借阅的书是:{bookname},借阅的数量是:{number}')


book_name('人', '小芳', school='北科')  # 使用关键字使得顺序不再一一对应
book_name('西游记', '小芳', 4, '北科')
