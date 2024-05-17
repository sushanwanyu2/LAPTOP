# @Time    : 2024/1/20 13:50
# @Author  : SU_SHAN_WAN_YU
# @File    : 测试.py
# @Description :
car_park = []
number = input('输入车牌号:')
# 构建结构{number:[0,x]}
car = {}
car[number] = [0]  # 字典名[key]=value,列表也可以作为值使用
car_park.append(car)
