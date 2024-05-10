# @Time    : 2024/1/17 12:27
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-4 字符串练习.py
# @Description :
'''
模拟文件上传，键盘输入文件名（anc.jpg），判断文件名(abc)是否达到六位以上
扩展名是不是.jpg.gif.png格式，如果不是提示上传失败，如
果名字不满足条件而扩展名满足条件，则随机生成一个6位数字组
成的文件名，打印成功上传××××××.XXX
'''
import random

# while True:
#     name = input('请输入上传文件全称：')
#     first_name = name[:-4]
#     print(first_name)
#     length = len(first_name)
#     result1 = name.endswith('.png')
#     result2 = name.endswith('.jpg')
#     result3 = name.endswith('.gif')
#
#     if length >= 6 and (result1 or result2 or result3):
#         print(f'{name}上传成功')
#         break
#     elif length < 6 and (result1 or result2 == True or result3 == True):
#         first_name1 = random.randint(100000, 999999)
#         last_name = name[-4:]
#         name = str(first_name1) + last_name
#         print('文件名不符合要求，已为你重新生成文件名，{}上传成功'.format(name))
#         break
#     else:
#         print('文件格式错误，请上传图片文件')
#
#
# print('*'*30)
# file = input('输入图片文件全称：')
# if file.endswith('jpg') or file.endswith('gif') or file.endswith('png'):
#     # 判断文件名
#     i = file.find('.')
#     name = file[:i]
#     if len(name) < 6:
#         m = random.randint(100000, 999999)
#         file = str(m) + file[i:]
#     print(f'{file}上传成功')
#
#
# else:
#     print('文件格式错误，请重新上传')

# 字母和数字的组合,验证码的产生

filename = ''
s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
for i in range(6):
    index = random.randint(0, len(s) - 1)
    filename += s[index]  # 借助随机产生的字符串下标找字母，拼到文件名上
print(filename)

s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
file = input('输入图片文件全称：')
if file.endswith('jpg') or file.endswith('gif') or file.endswith('png'):
    # 判断文件名
    i = file.find('.')
    name = file[:i]
    if len(name) < 6:
        name = ''
        for a in range(6):
            index = random.randint(0, len(s) - 1)
            name += s[index]  # 借助随机产生的字符串下标找字母，拼到文件名上
        file = name + file[i:]
    print(f'{file}上传成功')


else:
    print('文件格式错误，请重新上传')
