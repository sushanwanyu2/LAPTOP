# @Time    : 2024/1/25 10:42
# @Author  : SU_SHAN_WAN_YU
# @File    : 17-2 字典遍历和查询.py
# @Description :
'''
遍历和查询
list.index(),list.count() in
获取:
dict.get(key) 根据key获取value值
dict[key] 根据key获取value值
区别
1.get里面的key如果不存在,则返回None,还
.可以设置默认值,get(key,默认值)
2.dict[key] 会报错
遍历
# 如果直接使用使用for in 直接遍历字典,取出的是key
for i in book:
    print(i)  # 书名 价格等

book.values()获取所有的值存放到列表当中
for i in  book.values():
    print(i)
获取键值对 :字典.items()---->[(key.value),(),(),....]
for key,value in book.items():
    print(key,value)  分开获取
'''
book = {'书名': '《三体》', '价格': 36.0, '作者': '刘慈欣', '出版社': '科幻出版社'}
# 根据key得到value值
value = book.get('书名1')  # get有一个默认值,没找到的情况下返回
print(value)

# print(len(book))
value = book['书名']  # key错了会报错
print(value)
# # 如果使用for in 直接遍历字典,取出的是key
# for i in book:
#     print(i)  # 书名 价格等

# 获取字典所有的值
print(list(book.values()))  # ['《三体》', 36.0, '刘慈欣', '科幻出版社']

for i in book.values():
    print(i)

print(book.keys())

# 如何一对一对的拿出来
print(book.items())  # 一对一对放到元组里面
for it in book.items():
    print(it)
# 分开获取key和value
for key, value in book.items():
    print(key, value)

book.setdefault('历史', '唐代')  # 和book['历史']='唐代'相似
print(book)  # 只能做添加使用,不能用来修改
dict1 = {'a': 10, 'b': 20}
book.update(dict1)  # 将两个字典进行合并
print(book)
dict = book.fromkeys(['a', 'b'], 10)  # 构建一个新的字典
print(dict)

'''
books=[]能放多本书
书{}
书名,作者,价格
1.添加书
    不能添加同名书籍
2.循环添加三本书
'''
