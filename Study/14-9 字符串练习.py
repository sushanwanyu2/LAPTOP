# @Time    : 2024/1/19 10:57
# @Author  : SU_SHAN_WAN_YU
# @File    : 14-9 字符串练习.py
# @Description :
'''
模拟论坛：

'''
msg = input('发表一句话')
print('-' * 50)
print('以下为回复内容：')
while True:
    # 输入用户名
    username = input('输入用户名:')
    while True:
        # 输入回复内容
        comment = input('输入回复内容')
        comment = comment.strip()
        # 验证内容
        # 是否为空
        if len(comment) != 0:
            # 验证长度
            if len(comment) <= 20:
                # 是否存在敏感词
                comment = comment.replace('丑陋', '**')
                # 打印 \t代表缩进
                print('{}发表的评论是：\n\t{}'.format(username, comment))
                break
            else:
                print('评论不能超过20字')
        else:
            print('评论内容不能为空')
    # 成功则发出评论，否则重新输入
