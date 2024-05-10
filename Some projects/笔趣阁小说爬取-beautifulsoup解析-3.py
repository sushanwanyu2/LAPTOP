import requests
import os
import chardet
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

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
print(html_data.text)  # 打印看下数据内容
print(chardet.detect(html_data.content))  # 查看编码类型
soup = BeautifulSoup(html_data.text, 'lxml')  # 使用BeautifulSoup解析网页内容
author = input('请输入作者：')  # 获取作者信息
book_name = input('请输入小说名：')  # 获取小说名
# 通过分析页面结构，找到class属性为listmain的div标签
# 下面的每个dd标签中的跳转链接对应不同章节的url链接
# 获取’listmain‘这个div标签下的dd标签，每个dd标签下对应每章内容的url链接
divs = soup.select('.listmain dd')
result = ""  # 定义一个变量来保存运行结果
total_chapters = len(divs)  # 计算总章节数

def download_chapter(div):
    title = div.select_one('a').text  # 标题
    href = div.select_one('a')['href']  # 链接
    # 再把每章的内容拼接成一个完整的url链接
    url = 'https://www.quge9.cc' + href

    try:
        # 请求每章内容的URL
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'lxml')
        # 获取章节内容
        chapter_content = soup.select_one('#chaptercontent').text

        # 返回标题和内容
        return title, chapter_content
    # 如果请求失败，打印下报错内容到控制台，继续下次请求
    except Exception as e:
        print(e)


# 使用线程池来并发下载章节内容
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for div in divs:
        futures.append(executor.submit(download_chapter, div))

    # tqdm进度条
    with tqdm(total=total_chapters, desc="正在下载", ncols=80) as pbar:
        for future in futures:
            if future.result():
                title, chapter_content = future.result()
                result += f"{title}\n{chapter_content}\n\n"  # 在章节内容后添加两个换行符
                pbar.update(1)
                pbar.set_postfix({'当前章节': title})

# 将运行结果写入txt文档
with open(filename + book_name + '.txt', 'w', encoding='utf-8') as file:
    file.write(f"作者：{author}\n\n")
    file.write(result)

print('下载完成')
