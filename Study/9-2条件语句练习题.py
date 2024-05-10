# @Time    : 2024/1/13 13:07
# @Author  : SU_SHAN_WAN_YU
# @File    : 9-2条件语句练习题.py
# @Description :
'''
键盘上输入以下内容并打印输出：
默认（admin，1234）
用户名:username
密码：password
是否记住密码bool类型，is_remember
如果用户名和密码都正确并且is_remember是True表示记住密码，则打印
已经记住用户×××的密码，否则打印，没有记住密码，需要继续下次输入
'''
username = input('用户名：')
password = input('密码：')
is_remember = False

if username == 'admin' and password == '1234':
    if is_remember:
        print(f'已经记住用户{username}的密码')
    else:
        print('没有记住密码需要下次输入')
else:
    print('用户名或密码错误')

'''
模拟超市付款：商品单价  商品数量
键盘上输入商品单价以及商品数量
然后计算应付总额
计算总额 float
提示用户有四种不同的支付方式，具有不同折扣
现金支付无折扣
微信0.95折
支付宝 鼓励金付款金额的10%，可直接折算到付款金额当中
刷卡，满一百减20
'''
print('欢迎光临北科超市')
price = float(input('请输入商品单价：'))
number = int(input('输入数量'))
# 计算总额
total = price * number
# 选择付款方式
ways = input('选择付款方式：\n1.现金\n2.微信\n3.支付宝\n4.刷卡\n')
if ways == '1':
    print(f'现金支付没有折扣，应付{total:.2f}')
elif ways == '2':
    # 微信0.95折
    print('微信支付')
    total *= 0.95
    print('应付金额为{:.2f}'.format(total))
elif ways == '3':
    total *= 0.9
    print(f'支付宝支付，应付{total:.2f}')
elif ways == '4':
    total = total - (total // 100) * 20
    print('刷卡支付，应付{:.2f}'.format(total))
else:
    print('输入错误')
'''
----------if 补充---------
'''
a = 1
b = 2
if a < b:
    c = a
else:
    c = b
print(a, b, c)
# 等价与
a = 1
b = 2
c = a if a < b else b
print(a, b, c)

if '111':
    print('1111')
# ----------在python当中，只有0，'',"",None，{},[],会被转换成false
# 其余的都会转变为True。
if '':
    print(111)
else:
    print('0000')
