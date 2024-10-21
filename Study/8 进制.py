# @Time    : 2024/1/12 11:19
# @Author  : SU_SHAN_WAN_YU
# @File    : 8 进制.py
# @Description :
'''
二进制：0，1
八进制：0-7
十进制：0-9
十六进制：0-9，a-f

十进制转二进制表示：
bin() 0b
int()
oct() 0o
hex() 0x
'''
n = 149
result = bin(n)  # 转换为二进制
print(result)  # 0b表示二进制 binary 十进制转换为二进制

# 十进制转八进制 短除法除以八 八转十
result = oct(n)  # 十进制转八进制
print(result)
# 转十六进制
m = 221
res = hex(m)
print(res)
'''
bin
oct
hex
'''
# 前缀：0b二进制 0o八进制 0x十六进制
'''
1、n=0x558，如何转为十进制
2、转为二进制，转为八进制 
'''
n = 0x558
result = int(n)
print(result)

result = bin(n)
print(result)

x = 0b10101011000
print(bin(x))
print(oct(n))
print(hex(n))
'''
0x558--->二进制
0b 1010 1011000
'''
