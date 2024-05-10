# @Time    : 2024/3/29 22:01
# @Author  : SU_SHAN_WAN_YU
# @FileName: QW加解密.py
# @Software: PyCharm
# @Description


# qwe密码解密，输入字符串，返回解密的明文
def encrypt_qwe(s):
    DIC_QWE = "qwertyuiopasdfghjklzxcvbnm"
    DIC_ABC = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in s:
        for j in range(len(DIC_QWE)):
            if i == DIC_ABC[j]:
                result = result + DIC_QWE[j]
    return result


s = input('输入明文内容：')
s = s.lower()  # 统一转化为小写
s = s.strip().replace(" ", "")  # 去掉空格

print(encrypt_qwe(s))
