# @Time    : 2024/1/17 10:58
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-3 字符串.py
# @Description :关于判断的格式
'''
判断：startswith,endswith,isalpha(是不是字母),isdigit是不是数字,isalnum（字母或数字）,isspace（空格）
返回值都是布尔类型
startswith:判断是不是以啥开头
endswith：判断是不是以啥结尾
'''
s = '20240102020106.png'
result = s.startswith('abc')
print(result)
result1 = s.endswith('.png')
print(result1)

'''
模拟文件上传，键盘输入文件名，判断文件名是否达到六位以上
扩展名是不是.jpg.gif.png格式，如果不是提示上传失败，如
果名字不满足条件而扩展名满足条件，则随机生成一个6位数字组
成的文件名，打印成功上传××××××.XXX
'''
import random

while True:
    name = input('请输入上传文件名：')
    first_name = name[:-4]
    length = len(first_name)
    result1 = name.endswith('.png')
    result2 = name.endswith('.jpg')
    result3 = name.endswith('.gif')

    if length == 6 and (result1 == True or result2 == True or result3 == True):
        print(f'{name}上传成功')
        break
    elif length != 6 and (result1 == True or result2 == True or result3 == True):
        first_name1 = random.randint(100000, 999999)
        last_name = name[-4:]
        name = str(first_name1) + last_name
        print('文件名不符合要求，已为你重新生成文件名，{}上传成功'.format(name))
        break
    else:
        print('文件格式不符合要求，请重新输入')
print('*' * 40)

s = 'hello'
res = s.isalpha()  # 是否全部是字母组成，前提s必须是字符串
print(res)
s = '1234'
res = s.isdigit()
print(res)

s = 'q1233'
res = s.isalnum()
print(res)
s = '   '
res = s.isspace()  # 判断是否全部由纯空格组成
print('res')

s = 'HELLO'
res = s.isupper()
res = s.islower()
print(res)
'''
admin123
15811119999 200325
用户名或者手机号码登陆+密码
用户名：全部小写，首字母不能是数字，长度必须是6位以上
手机号码：纯数字，长度11
密码必须是6位数字
若符合要求，则进入下层的正确性验证，用户名和密码是否正确

'''
