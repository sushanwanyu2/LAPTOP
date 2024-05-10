# @Time    : 2024/1/24 12:20
# @Author  : SU_SHAN_WAN_YU
# @File    : 16-1王者荣耀角色管理.py
# @Description :
'''
王者荣耀角色管理

角色:姓名,性别,职业
添加角色
删除角色
修改角色
查询角色:输入人名找到相关介绍
显示所有角色
退出管理系统
'''
import time

all_role = []  # 存放所有角色的容器
print('----------欢迎进入王者荣耀角色管理----------')
while True:
    choice = input('请选择功能:\n1.添加角色\n2.删除角色\n3.修改角色\n4.查询角色\n5.显示所有角色\n6.退出系统\n')
    if choice == '1':
        print('添加角色模块')
        name = input('\t角色姓名:')
        sex = input('\t性别:')
        job = input('\t职业:')
        role = [name, sex, job]
        all_role.append(role)
        print(f'\t成功添加{name}到王者荣耀系统\n')
    elif choice == '2':
        print('删除角色模块')
        role_name = input('输入角色名:')
        # 查找是否存在此角色名称
        for role in all_role:  # [['赵飞','男','法师'],[],[]]
            if role_name in role:  # ['赵飞','男','法师']
                # 添加是否删除的询问
                answer = input('是否确定删除(1.是 2.否):')
                if answer == '1':
                    all_role.remove(role)
                    print('成功删除角色:{}'.format(role_name))
                    break
        else:
            print(f'本系统不存在角色:{role_name},请检查角色名称.')
    elif choice == '3':
        print('角色修改模块')
        gai = input('输入要修改的角色名称:')
        for role in all_role:
            if gai in role:
                answer1 = input('要修改:1.姓名2.性别3.职业')
                if answer1 == '1':
                    role[0] = input('新姓名:')

                elif answer1 == '2':
                    role[1] = input('新性别:')

                elif answer1 == '3':
                    role[2] = input('新职业:')

                else:
                    print('输入错误')
                print('修改成功,新信息如下:{}{}{}'.format(role[0].ljust(10), role[1].ljust(10), role[2].ljust(10)))
                break
        else:
            print(f'本系统不存在角色:{gai},请检查角色名称.')
    elif choice == '4':
        print('查询模块')
        role_name = input('输入要查询的角色名:')
        #     查找是否存在此角色名称
        for role in all_role:  # [['赵飞','男','法师'],[],[]]
            if role_name in role:  # ['赵飞','男','法师']
                print('存在此角色,信息如下:')
                print('{}{}{}'.format(role[0].ljust(10), role[1].ljust(10), role[2].ljust(10)))
                break
        else:
            print(f'本系统不存在角色:{role_name},请检查角色名称.')
    elif choice == '5':
        print('显示所有角色模块')
        print('{}{}{}'.format('名称'.center(10), '性别'.center(10), '职业'.center(10)))
        for role in all_role:
            print(role[0].center(10), end='')
            print(role[1].center(10), end='')
            print(role[2].center(10), end='')
            print()
    elif choice == '6':
        print('正在退出王者荣耀管理系统~~~~~~')
        time.sleep(2)  # 表示休眠3秒
        print('退出成功!')
        break
    else:
        print('输入错误,请重新选择')
