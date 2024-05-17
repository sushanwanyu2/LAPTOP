# @Time    : 2024/5/17 下午3:14
# @Author  : SU_SHAN_WAN_YU
# @FileName: 18-12 停车计费系统.py
# @Software: PyCharm
# @Description
'''
time函数的使用：
time.time()返回当前时间的时间戳
time.ctime([secs])：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。
如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
'''
'''
题目:
停车计费系统:
进入停车场记录进入时间,出去记录出去时间,停车时间是出-进
停车场数据结构是[{'车牌':[进入时间,出去时间]}],为方便进入时间为0
15min 1块
停车变量,全局变量
'''
import random

# 一开始没有车辆
car_park = []


# while True:
#     # 进场
#     pass

def enter():
    print('欢迎进入xxx停车场')
    number = input('输入车牌号:')
    # 构建结构{number:[0,x]}
    car = {}
    car[number] = [0]  # 字典名[key]=value，列表也可以作为值使用
    # 添加到car_park
    car_park.append(car)
    print('{}进场'.format(number))


def out():
    number = input('输入车牌号:')
    # 判断车辆是否进场
    for car in car_park:
        if number in car:
            # 记录结束时间
            time = random.randint(0, 24)
            # dict.get(key) 根据key获取value值
            time_record = car.get(number)
            time_record.append(time)
            # 计算花费
            total = time * 4
            print(f'{number}停车{time}小时,应缴费{total}元')
            break
    else:
        print('此车未进场')


enter()
enter()
enter()
out()
out()
out()
print(car_park)
