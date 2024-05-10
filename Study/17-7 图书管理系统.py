# @Time    : 2024/1/26 11:38
# @Author  : SU_SHAN_WAN_YU
# @File    : 17-7 图书管理系统.py
# @Description :
'''
图书管理系统
至少5本书
library = [{'bookname':,'author':,'price':10,'number':4},{'bookname':}},{},{}]
1.借书
2.还书
3.查询(书名/作者)
4.查看所有
5.退出
'''
import time

list1 = []  # 符合条件的书籍列表
print('----欢迎进入图书管理系统----')
library = [{'bookname': '围城', 'author': '钱钟书', 'price': 40, 'number': 3},
           {'bookname': '白说', 'author': '白岩松', 'price': 30, 'number': 5},
           {'bookname': '红楼梦', 'author': '曹雪芹', 'price': 37, 'number': 3},
           {'bookname': '西游记', 'author': '吴承恩', 'price': 35, 'number': 3},
           {'bookname': '三国演义', 'author': '罗贯中', 'price': 58, 'number': 18},
           {'bookname': '三国演义', 'author': 'xxxxx', 'price': 28, 'number': 7}]
while True:
    choice = input('选择服务:\n\t1.借书\n\t2.还书\n\t3.查询\n\t4.查看所有库存\n\t5.退出\n')
    if choice == '1':
        print('---借书模块---')
        answer = input('输入要借的书名:')
        print(f'{"bookname".ljust(13)}{"author".ljust(10)}{"price".ljust(10)}{"number".ljust(10)}')
        for book in library:
            result1 = list(book.values())
            if result1[0] == answer:
                # 打印出符合条件的图书
                print(result1[0].ljust(10), result1[1].ljust(9), str(result1[2]).ljust(10),
                      str(result1[3]).ljust(10),
                      end='')
                print()
                list1.append(result1)
        if len(list1) == 0:
            print('该书籍不存在或输入的书籍名有误')
        print(list1)
        if len(list1) > 1:
            author_choice = input('输入要借阅书籍的作者名:')
            for book in library:  # 遍历所有图书
                if book.get('bookname') == answer and book.get('author') == author_choice:
                    book['number'] -= 1
                    print(f'{book["bookname"]}借阅成功')
                    break
            else:
                print('作者输入错误')
        elif len(list1) == 1:
            for book in library:  # 遍历所有图书
                if book.get('bookname') == answer:
                    book['number'] -= 1
                    print(f'{book["bookname"]}借阅成功')
        list1.clear()
    elif choice == '2':
        print('---还书模块---')
        book_name=input('输入要还的书名:')
        book_author=input('输入该书的作者:')
        for book in library:  # 遍历所有图书
            if book.get('bookname') == book_name and book.get('author') == book_author:
                book['number'] += 1
                print(f'{book["bookname"]}还书成功')
                break
        else:
            print('输入有误或不存在该书')
    elif choice == '3':
        print('---图书查询模块---')
        choice1 = input('\t1.以书名查询\n\t2.以作者查询\n')
        if choice1 == '1':
            answer = input('输入要查询的书名:')
            print(f'{"bookname".ljust(13)}{"author".ljust(10)}{"price".ljust(10)}{"number".ljust(10)}')
            for book in library:
                result1 = list(book.values())
                if result1[0] == answer:
                    # 打印出符合条件的图书
                    print(result1[0].ljust(10), result1[1].ljust(9), str(result1[2]).ljust(10),
                          str(result1[3]).ljust(10),
                          end='')
                    print()
                    list1.append(result1)
            if len(list1) == 0:
                print('该书籍不存在或输入的书籍名有误')
            list1.clear()
        elif choice1 == '2':
            answer = input('输入要查询的作者:')
            print(f'{"bookname".ljust(13)}{"author".ljust(10)}{"price".ljust(10)}{"number".ljust(10)}')
            for book in library:
                result1 = list(book.values())
                if result1[1] == answer:
                    # 打印出符合条件的图书

                    print(result1[0].ljust(10), result1[1].ljust(8), str(result1[2]).ljust(10),
                          str(result1[3]).ljust(10),
                          end='')
                    print()
                    list1.append(result1)
            if len(list1) == 0:
                print('该书籍不存在或输入的书籍名有误')
            list1.clear()

    elif choice == '4':
        print(f'{"bookname".ljust(13)}{"author".ljust(10)}{"price".ljust(10)}{"number".ljust(10)}')
        for a in library:  # 遍历打印所有图书库存
            result = list(a.values())
            print(result[0].ljust(10), result[1].ljust(8), str(result[2]).ljust(10), str(result[3]).ljust(10), end='')
            print()
    elif choice == '5':
        print('正在退出图书管理系统~~~~~')
        time.sleep(2.5)
        print('退出成功')
        break
    else:
        print('输入错误,请重新选择服务')
