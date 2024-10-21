# @Time    : 2023/8/10 10:51
# @Author  : SU_SHAN_WAN_YU
# @File    : 7 格式化输出.py
# @Description :
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name.title() + ' ' + last_name.title()

print(full_name)

# + 用来连接字符串，.title（）用来将首字母变为大写，.lower用来将所有变为小写
# .upper所有变为大写
# \t代表制表位，\n代表空行

print('\tpython')
print('\npython')
# 删除空白
word = 'python '
print(word.rstrip())
print(word)
word1 = word.rstrip()
print(word1)
# .rstrip()代表删除末尾空白
# .lstrip()代表删除开头空白
# .strip()代表删除所有空白
name = '蔡徐坤'
age = 26
# 我喜欢听26岁的蔡徐坤唱歌
print('我喜欢听' + str(age) + '岁的' + name + '唱歌')
# 字符串如何进行输出
'''
符号：
%s 字符串 string
%d 整数 digit
%f 浮点数 float
'''
print('我喜欢听%d岁的%s唱歌' % (age, name))

money = 999.99
# 26岁的蔡徐坤一首歌挣了999.99元

print('%d岁的%s一首歌挣了%f元' % (age, name, money))

print('%s岁的%s一首歌挣了%s元' % (age, name, money))

print('%d岁的%s一首歌挣了%.2f元' % (age, name, money))  # %.2f保留两位小数
print(f'{age}岁的{name}一首歌挣了{money:.2f}元')
'''
f-string格式化
f-string格式化是在Python3.6之后引入的一种新的字符串格式化方式，这种格式化方式使用非常简单，只需要在字符串前面加上 f 或F ，
并用花括号 {} 在字符串中表示要被替换的变量，其中花括号 {} 内直接填入要替换的变量。数据类型代号和辅助符号用冒号:连接在在变量的后面，可以不填。

name = '周杰伦'
age = 28
print(f"大家好，我是{name}，今年{age}岁")
输出：

good_percent = 98.6529
print(f'好评率是{good_percent}%')
print(f'好评率是{good_percent:.2f}%')
输出：


使用f-string格式化时，要注意花括号内使用的引号不能与花括号外的引号定界符冲突！
简单说，只要花括号内外的引号不同，就没有问题。但是花括号中只用单引号和双引号，花括号外的引号定界符可以使用单引号、双引号、单三引号、双三引号。

如下面的程序中，为了满足花括号内外的引号不同，花括号外的引号定界符使用的是单引号，那么花括号内的引号只能用双引号，不能再使用单引号！

person = {'name': '周杰伦', 'age': 28, 'hobby': '唱歌'}
print(f'大家好，我是{person["name"]}，今年{person["age"]}岁，我的爱好是{person["hobby"]}。')


花括号外的引号定界符使用的是单三引号或双三引号可以打印多行字符串，这时花括号内既可以使用单引号还可以使用双引号。

person = {'name': '周杰伦', 'age': 28, 'hobby': '唱歌'}
print(f"""大家好，
我是{person["name"]}，
今年{person[‘age’]}岁，
我的爱好是{person["hobby"]}。
""")


f-string格式化还可以对date、datetime和time等时间对象进行年月日、时分秒等格式化地打印。
注意，花括号外如果想要打印花括号，需要输入连续两个花括号。

from datetime import datetime
 
 
print(f'今天是{datetime.today()}')
print(f'今天是{datetime.today():%Y-%m-%d}')
print(f'{{今天}}是{datetime.today():%Y-%m-%d}')

如果在f-string的花括号内填入可执行的程序语句，如计算表达式等，则在格式化时会求出其结果并填入字符串内。

a = 2
b = 5
print(f'{a} × {b} = {a * b}')


f-string的优雅之处

相比于占位符格式化，f-string使用花括号加变量的方式，更加容易理解可读性更强。

由于f-string直接使用到了变量进行标记，所以可以不用关心变量占位的顺序，避免了可能的顺序错乱的问题。

f-string在花括号中可以使用可执行的程序语句，这使得在格式化占位时更加灵活方便。

Python版本在3.6以上的小伙们，推荐多使用f-string这种新的字符串格式化方法。
'''
from datetime import datetime

print(f'今天是{datetime.today()}')
print(f'今天是{datetime.today():%Y-%m-%d}')
print(f'{{今天}}是{datetime.today():%Y-%m-%d}')
