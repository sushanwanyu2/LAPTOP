# @Time    : 2024/1/18 12:08
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-5字符串练习.py
# @Description :
'''
admin123
15811119999 200325
用户名或者手机号码登陆+密码
用户名：全部小写，首字母不能是数字，长度必须是6位以上
手机号码：纯数字，长度11
密码必须是6位数字
若符合要求，则进入下层的正确性验证，用户名和密码是否正确

'''

# name = input('用户名或手机号码：')
# # 判断
# if 验证是否符合用户名的规则 or 是否符合手机号码的规则:
#     # 继续输入密码
#     password= input('输入密码：')
#     if 判断是否是6位数字:
#         # 验证正确性
#         pass
#     else:
#         print('密码必须是6位数字')
#
# else:
#     print('用户名或者手机号码格式错误！')
'''
admin123
15811119999 200325
用户名或者手机号码登陆+密码
用户名：全部小写，首字母不能是数字，长度必须是6位以上
手机号码：纯数字，长度11
密码必须是6位数字
若符合要求，则进入下层的正确性验证，用户名和密码是否正确

'''
flag = True  # 添加变量便于结束外层的循环
while flag:
    name = input('用户名或手机号码：')
    # 判断
    if name.islower() and name[0].isalpha() and len(name) >= 6 or name.isdigit() and len(name) == 11:
        while True:
            # 继续输入密码
            password = input('输入密码：')
            if password.isdigit() and len(password) == 6:
                # 验证正确性
                if int(password) == 200325 and (name == 'admin123' or name == '15811119999'):
                    print('登陆成功')
                    flag = False  # 通过添加一个变量结束外面一层的循环
                else:
                    print('登陆失败，用户名和密码不匹配')
                break  # 结束第二个循环，回到第一个循环
            else:
                print('密码必须是6位数字,重新输入')
    else:
        print('用户名或者手机号码格式错误！请重新输入')
