# @Time    : 2024/2/1 10:59
# @Author  : SU_SHAN_WAN_YU
# @File    : 18-6 可变参数-1.py
# @Description :
'''
可变参数:**kwargs
关键字参数
在函数调用的时候必须传关键字才可以转换成key:value
装到字典中
'''


def show_book(**kwargs):
    print(kwargs)  # {}
    for k, v in kwargs.items():
        print(k, v)


show_book()  # 调用的时候得使用关键字参数赋值调用
show_book(bookname='红楼梦', author='曹雪芹', number=9)  # {'bookname': '红楼梦', 'author': '曹雪芹'}
print('-'*40)
book = {'bookname': '红楼梦', 'author': '曹雪芹', 'number': 9}
show_book(**book)  # 拆包


