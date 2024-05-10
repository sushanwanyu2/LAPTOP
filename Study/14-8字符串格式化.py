# @Time    : 2024/1/19 10:31
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-8字符串格式化.py
# @Description :
'''
格式化：
1.%d %f %s...
print('李泽说：%s'%xxx)
2.format
'''

name = '123'
age = 18
print('某人{}今年{}岁'.format(name, age))  # 变量用数字代替进行复用
# 用数字进行多次的调用
# 使用数字填充索引，从0开始计数
print('某人{0}今年{1}岁，我也是{1}岁'.format(name, age))

# 变量名的形式，format的参数必须是关键字参数
print('某人{name}今年{age}岁，我也是{age}岁'.format(name='123', age=19))

name = '小明'
score_chinese = 100
score_math = 99

s = '{0}数学{2}分，语文{1}分，英语也是{2}分'.format(name, score_chinese, score_math)
print(s)
s = f'{name}数学{score_math}分，语文是{score_chinese}英语也是{score_math}'.format(name='小明', score_chinese=100, score_math=99)
print(s)
