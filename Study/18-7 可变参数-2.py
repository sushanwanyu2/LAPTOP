# @Time    : 2024/2/1 12:31
# @Author  : SU_SHAN_WAN_YU
# @File    : 18-7 可变参数-2.py
# @Description :
'''
*args  **kwargs
同时存在。
arguments
'''


def show_book(*args, **kwargs):
    print(args)  # ()不带关键字
    print(kwargs)  # {}带关键字,键值对


show_book()
book = {'bookname': '红楼梦', 'author': '曹雪芹', 'number': 9}
show_book('龙少', '小芳', **book)
print('{}{}{}'.format('aa', '方法', '得到'))

print('*'.join({'三', '东方红郡'}))  # 崔*东方红郡 里面放的可迭代的,例如列表等
print(type('*'.join({'三', '东方红郡'})))  # <class 'str'>
