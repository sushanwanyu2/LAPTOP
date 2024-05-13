# @Time    : 2024/5/13 下午8:00
# @Author  : SU_SHAN_WAN_YU
# @FileName: 18-11 可变和不可变类型.py
# @Software: PyCharm
# @Description
'''
加global的条件:
需不需要加global,看变量是可变还是不可变
只有是不可变的才需要加global
可变的不需要加global.
可变类型:
不可变类型:
'''
library = ['红楼梦', '西游记', '水浒传']


def add_book(book_name):
    if book_name in library:
        print('该书已经存在')
    else:
        library.append(book_name)
        print('添加成功')


def show_book():
    print('图书馆书籍如下')
    for book in library:
        print(book)


show_book()
add_book('三国演义')

# 可变和不可变
a = 100
print(id(a))
a = 80
print(id(a))  # 二者地址不同
