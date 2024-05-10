# @Time    : 2024/1/20 13:50
# @Author  : SU_SHAN_WAN_YU
# @File    : 测试.py
# @Description :
library = [{'bookname': '围城', 'author': '钱钟书', 'price': 40, 'number': 3},
           {'bookname': '白说', 'author': '白岩松', 'price': 30, 'number': 5},
           {'bookname': '红楼梦', 'author': '曹雪芹', 'price': 37, 'number': 3},
           {'bookname': '西游记', 'author': '吴承恩', 'price': 35, 'number': 3},
           {'bookname': '三国演义', 'author': '罗贯中', 'price': 58, 'number': 2}]
print(f'{"bookname".ljust(15)}{"author".ljust(10)}{"price".ljust(10)}{"number".ljust(10)}')
for i in library:
    result = list(i.values())
    print(result[0].ljust(13), result[1].ljust(8), str(result[2]).ljust(10), str(result[3]).ljust(10), end='')
    print()
