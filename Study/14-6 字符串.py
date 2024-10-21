# @Time    : 2024/1/18 12:55
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-6 字符串.py
# @Description :
'''
替换内容：replace
切割字符串：split，rsplit,splitlines,partition,rpartition
split（’分隔符‘，maxsplit）结果存在列表中 maxsplit最大切割次数

修改大小写：capitalize(全句首字母大写)，title（首字母大写），upper，lower
capitalize 第一个单词首字母大写

'''
# 替换李泽和阿烁 通过正则表达式来搞定，或者是使用循环（学完列表来处理）
s = '李泽说：阿烁你来唱歌吧,阿烁你来唱歌吧'
result = s.replace('阿烁', '**', 1)  # 默认全部替换，也可以通过count指定替换个数
print(result)

s = '李泽 阿烁 郭琦'
result = s.split(' ')  # 调用split存在列表中
print(result)

s = '''阿烁你来唱歌吧
阿烁你来跳舞吧
阿烁你来吃饭吧
阿烁你来学习吧
'''
result = s.splitlines()
print(result)
s = '李泽 阿烁 郭琦'
result = s.partition(' ')  # 分隔成三部分

print(result)
# 大小写转换
s = 'hello'
result = s.title()
print(result)
result = s.upper()
s = 'hello world'
result = s.capitalize()
print(result)


'''
cyc
'''