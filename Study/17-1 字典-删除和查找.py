# @Time    : 2024/1/25 10:18
# @Author  : SU_SHAN_WAN_YU
# @File    : 17-1 字典-删除和查找.py
# @Description :
'''
字典删除:
pop(key)
popitem()
clear()清空
del 字典名[key]
'''
# 该字典表示一本书的信息
book = {'name': '三体', '价格': 36.0, '作者': '刘慈欣', '出版社': '科幻出版社'}
# book.clear()
# print(book)
# pop删除,删除键值对
# r = book.pop('出版社')  # 找到对应的key,删除元素
# print(book)  # 根据key删除键值对


# r = book.popitem()  # 无需传任何参数
# print(r)  # 返回值是一个元组('出版社', '科幻出版社')
# print(book)  # 从后往前删除
del book['价格']
print(book)

# del book  # 删除整个字典结构
'''
books=[{},{},{}....]
book={}
书名 价格 作者 出版社
删除每本书里面的出版社信息
'''
books = [
    {'name': '三体', '价格': 36.0, '作者': '刘慈欣', '出版社': '科幻出版社'},
    {'name': '流浪地球', '价格': 56.0, '作者': '刘慈欣', '出版社': '科幻出版社'}
]
print(books)

for i in books:  # i 是一个字典

    i.pop('出版社')
print(books)
