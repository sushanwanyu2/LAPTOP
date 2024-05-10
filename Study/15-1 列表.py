# @Time    : 2024/1/19 12:26
# @Author  : SU_SHAN_WAN_YU
# @File    : 15-1 列表.py
# @Description :
s = 'abcd123'
for i in range(10):
    print(i, end='*')
print('')
for i in s:
    print(i, end='*')
print('')
s = 0
for i in 'jd8f373j8':
    if i.isdigit():
        s += int(i)
print(s)
# 字符串的操作：
# len,find,rfind,startswith,endswith,isalpha,isdigit,....

'''
列表的增删改查
1.列表添加元素
'''
# 元素的增加
list1 = []
list2 = ['面包']

list1.append('火腿肠')
print(list1)
list1.append('酸奶')
list1.append('辣条')
print(list1)

list2.append('薯条')
print(list2)
list1 = list1 + list2  # 两个列表合并，加号就可以
print(list1)
'''
加号的用处：
数字的加和 n=1+3
字符串的拼接 s='aa'+'bb'
列表的拼接 list = [1,2,3]+[2,3,4]
'''
list1.extend(list2)  # 两个列表合并的第二种方法
print(list1)

'''
买多件：
商品名称， 价格， 数量
要用到列表的嵌套
'''
container = []  # 存放多件商品的容器
count = 0
total = 0
flag = True
while flag:
    # 添加商品
    name = input('商品名称：')
    price = input('商品价格：')
    number = input('商品数量：')
    goods = [name, price, number]
    count += int(number)  # 计件
    total += float(price) * int(number)  # 计算总价格
    # 添加到container里面
    container.append(goods)  # append没有拆散，expend拆散
    answer = input('是否继续添加，按q或Q退出')
    if answer.lower() == 'q':
        flag = False
print('*' * 30)
# 遍历container里的内容
print('商品名'.center(10), '价格'.center(10), '数量'.center(10), sep='')
for goods in container:
    print(f'{goods[0]}'.center(10), f'{float(goods[1]):.2f}'.center(15), f'{goods[2]}'.center(8), sep='')

print(f'总量'.center(10), ' ' * 12, f'{count}'.center(12), sep='')
print(f'总价'.center(10), ' ' * 12, f'{total:.2f}'.center(12), sep='')
