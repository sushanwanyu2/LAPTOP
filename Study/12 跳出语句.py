# @Time    : 2024/1/15 11:39
# @Author  : SU_SHAN_WAN_YU
# @File    : 12 跳出语句.py
# @Description :
'''
break  跳出整个循环
continue 继续执行循环，跳过后面的语句
'''
# 不打印能被三整除的数
# for i in range(10):
#     if i % 3 != 0:  # 不等于
#         print(i)

for i in range(10):
    if i % 3 == 0:
        continue
    print(i)
print('#' * 30)
for i in range(1, 10):
    if i % 3 == 0:
        break
    print(i)
