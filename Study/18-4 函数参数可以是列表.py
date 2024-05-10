# @Time    : 2024/1/30 11:19
# @Author  : SU_SHAN_WAN_YU
# @File    : 18-4 函数参数可以是列表.py
# @Description :
'''

'''
library = ['python精通', 'MysQl', '数据分析', '人工智能']


# 形参
def add_book(bookname):
    library.append(bookname)
    print('图书添加成功!')


def show_book(library):
    for books in library:
        print(books)


# 调用
add_book('新概念英语')
show_book(library)  # 参数可以是列表

list1 = [23, 45, 88, 59, 10]

# 获取大于50的数。
def get_list(list_1):
    # new_list = []
    # for i in list_1:
    #     if i >= 50:
    #         new_list.append()
    new_list = [e for e in list_1 if e >= 50]
    print(new_list)


get_list(list1)


def remove_from_list(list_1):
    n = 0
    while n < len(list_1):
        if list_1[n] < 50:
            list_1.remove(list_1[n])
        else:
            n += 1
    print(list1)


remove_from_list(list1)
