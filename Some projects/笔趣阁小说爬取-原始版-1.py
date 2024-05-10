import requests
import parsel
import os
import chardet

# 设置保存小说的文件夹
filename = '../小说\\'

# 创建这个文件夹时先判断是否有同名文件夹
# 如果没有.创建,有,则在已有文件夹保存
if not os.path.exists(filename):
    os.mkdir(filename)

# 给爬虫设置请求头。模拟浏览器访问
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

# 分析网页结构可知，每本书有对应ID链接加ID就能到书籍页面
rid = input('输入书名ID:')
link = f'https://www.quge9.cc/book/{rid}/'
# 用request对目标url发送请求，带上请求头，并通过TXT属性获取响应的文本内容
html_data = requests.get(url=link, headers=headers)
html_data.encoding = html_data.apparent_encoding  # 防止乱码
# 打印看下数据内容
print(html_data.text)
print(chardet.detect(html_data.content))  # 查看编码类型
book_name = input('请输入小说名：')
# 使用parsel里的selector类初始化一个文档选择器，就可以通过结构化语法获取对于标签内容
selector_2 = parsel.Selector(html_data.text)
# 通过分析页面结构，找到class属性为listmain的div标签
# 下面的每个dd标签中的跳转链接对应不同章节的url链接
# 获取’listmain‘这个div标签下的dd标签，每个dd标签下对应每章内容的url链接
divs = selector_2.css('.listmain dd')

# 定义一个变量来保存运行结果
result = ""

# 循环所有的dd标签，每次循环获取每个章节的标题 和链接所在的标签下的属性
for div in divs:
    # 标题
    title = div.css('a::text').get()
    # 链接
    href = div.css('a::attr(href)').get()
    # 再把每章的内容拼接成一个完整的url链接
    url = 'https://www.quge9.cc' + href

    # 再对每章内容的URL发送请求，为防止标签无效的情况，在请求外层套一个异常捕获语句结构
    try:
        # 如果能够捕获到，则拿到的响应的文本内容提取文本内容
        response = requests.get(url=url, headers=headers)
        selector = parsel.Selector(response.text)
        # getall返回的是一个包含文本的列表[]
        book = selector.css('#chaptercontent::text').getall()
        # 所以我们把每一句内容通过换行符连接在一起
        book = '\n'.join(book)
        # 将每章节的内容添加到结果变量中
        result += f"{title}\n{book}\n"

        print('正在下载章节：', title)
    # 如果请求失败，打印下报错内容到控制台，继续下次请求
    except Exception as e:
        print(e)

# 将运行结果写入txt文档
with open(filename + book_name + '.txt', 'w', encoding='utf-8') as file:
    file.write(result)
print('下载完成')
