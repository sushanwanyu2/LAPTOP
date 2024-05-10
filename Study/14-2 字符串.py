# @Time    : 2024/1/17 10:37
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-2 字符串.py
# @Description :
'''
https://img-home.csdnimg.cn/images/20240102020106.png
find:从左向右找，只要遇到符合要求的则返回位置。若没有找到任何符合要求的则返回-1
index：没找到会报错（与find的唯一区别）
rfind：从右往左找，遇到符合要求的则返回位置
rindex：
count:计算字符串里出现的次数,统计指定字符的个数
在字符串里找多个字符
'''
path = 'https://img-home.csdnimg.cn/images/20240102020106.png'
start = path.find('2')
print(start)
image_name = path[start:]
print(image_name)  # 拿到图片名
i = path.rfind('.')
zhui = path[i:]
print(zhui)  # 拿到图片后缀名
'''
找一个字符串里面有几个点
count:计算字符串里出现的次数,统计指定字符的个数
'''
n = path.count('.')
print('n=', n)
# 找多个字符
m = path.find('images')  # 返回第一个字母的位置
