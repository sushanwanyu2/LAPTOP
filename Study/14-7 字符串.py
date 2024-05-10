# @Time    : 2024/1/19 10:13
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-7 字符串.py
# @Description :
'''
空格处理：ljust放在30个字符左侧
rjust放在30个字符右侧
center 控制字符串对齐方式 放在30个字符中间
lstrip 左侧的空格
rstrip 右侧的空格
strip 去除左右两侧的空格
字符串拼接：join ['','','',]列表调用最终返回字符串
'''

# username = input('输入用户名：')
# print(len(username))
# 经常使用的是strip
s = ' adm in '
print(len(s))
result = s.strip()
print(len(result))

s = 'hello world'
result = s.center(30)  # 放在30个字符中间
print(result)

result = s.ljust(30)  # 放在30个字符左侧
print(result)

result = s.rjust(30)  # 放在30个字符右侧
print(result)

b = 'avc'
c = 'vbf'
