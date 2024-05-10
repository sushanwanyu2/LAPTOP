# @Time    : 2024/1/25 11:56
# @Author  : SU_SHAN_WAN_YU
# @File    : 17-3 字典讲解.py
# @Description :
'''
books=[]能放多本书
书{}
书名,作者,价格
1.添加书
    不能添加同名书籍
2.循环添加三本书
'''
# # 书写方式1
# books = []
# while True:
#     # 判断是不是已经到三本书
#     if len(books) == 3:
#         break
#     book = {}
#     name = input('输入书名:')
#     # 判断是否已经存在该书
#     for i in books:
#         if name == i.get('书名'):
#             print('书名重复')
#             break
#     else:
#         book['书名'] = name
#         book['作者'] = input('输入作者:')
#         book['价格'] = input('输入价格:')
#         books.append(book)
#
# print(books)
# 书写方式2
books = []
while True:
    book = input('请输入要添加的书名,作者,价格,以空格隔开:').split(' ')  # ['','','']
    for i in books:
        if i['书名'] == book[0]:  # 在一个字典中根据key取出值与book中的值作比较
            print(f'{book[0]}已存在,已跳过此选项')
            break
    else:
        books.append({'书名': book[0], '作者': book[1], '价格': book[2]})
    if len(books) == 3:
        break
print(books)
