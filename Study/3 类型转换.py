# @Time    : 2023/8/9 20:36
# @Author  : SU_SHAN_WAN_YU
# @File    : 3 类型转换.py
# @Description :
# input()输入语句  阻塞型函数

userName = input('请输入你的用户名：')
print(type(userName))  # input里面的输入全部都是字符串

# 类型转换
money = input('money=')
print(int(money)+1000)
print(money+str(1000))
'''
以变量名a
str转int str转float 
int转str  float转int（小数点后的数被抹除）
布尔类型的转换，T为1，F为0，转int的时候
只有0和空字符串的的时候转化为布尔类型才会转化为False，
其他的只要变量有值就会转换为Ture
'''