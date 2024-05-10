import tkinter as tk
from tkinter import ttk
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import os
import requests
import parsel
from PIL import Image, ImageTk

class NovelDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("小说下载器")

        self.root.iconbitmap('icon.ico')  # 添加图标

        self.url_label = ttk.Label(root, text="请输入书名ID:", font=("楷体", 12, "bold"))
        self.url_label.pack()

        self.url_entry = ttk.Entry(root, font=("楷体", 12))
        self.url_entry.pack()

        self.author_label = ttk.Label(root, text="请输入作者:", font=("楷体", 12, "bold"))
        self.author_label.pack()

        self.author_entry = ttk.Entry(root, font=("楷体", 12))
        self.author_entry.pack()

        self.book_label = ttk.Label(root, text="请输入小说名:", font=("楷体", 12, "bold"))
        self.book_label.pack()

        self.book_entry = ttk.Entry(root, font=("楷体", 12))
        self.book_entry.pack()

        self.download_button = ttk.Button(root, text="下载小说", command=self.download_novel, style="Download.TButton")
        self.download_button.pack()

        self.output_label = ttk.Label(root, text="下载进度:", font=("楷体", 12, "bold"))
        self.output_label.pack()

        self.output_text = tk.Text(root, height=10, width=50, font=("楷体", 10))
        self.output_text.pack()

        self.style = ttk.Style()
        self.style.configure("Download.TButton", font=("楷体", 12, "bold"), background="#4CAF50", foreground="black", padding=10)

        self.progress_var = tk.StringVar()
        self.progress_label = ttk.Label(root, textvariable=self.progress_var, font=("楷体", 12, "bold"))
        self.progress_label.pack()

        self.update_progress()

    # 添加一个新的方法update_progress
    def update_progress(self):
        if self.progress_var.get() != "下载进度: 完成":
            self.progress_label.update_idletasks()
            self.root.after(100, self.update_progress)
    def download_novel(self):
        rid = self.url_entry.get()
        author = self.author_entry.get()
        book_name = self.book_entry.get()

        # ... (略去下载函数的部分)
        # 创建文件夹
        filename = '../小说\\'
        if not os.path.exists(filename):
            os.mkdir(filename)

        # 设置请求头信息
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }

        # 构建小说链接
        link = f'https://www.quge9.cc/book/{rid}/'
        html_data = requests.get(url=link, headers=headers)

        # 解析小说章节链接
        selector = parsel.Selector(html_data.text)
        divs = selector.css('.listmain dd')
        total_chapters = len(divs)

        result = ""

        def download_chapter(div):
            title = div.css('a::text').get()
            href = div.css('a::attr(href)').get()
            url = 'https://www.quge9.cc' + href

            try:
                response = requests.get(url=url, headers=headers)
                response.encoding = response.apparent_encoding

                selector = parsel.Selector(response.text)
                book = selector.css('#chaptercontent::text').getall()
                book = '\n'.join(book)

                return title, book

            except Exception as e:
                print(e)
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for div in divs:
                futures.append(executor.submit(download_chapter, div))

            with tqdm(total=total_chapters, desc="正在下载", ncols=80) as pbar:
                for idx, future in enumerate(futures):
                    if future.result():
                        title, book = future.result()
                        result += f"{title}\n{book}\n"
                        pbar.update(1)
                        pbar.set_postfix({'当前章节': title})
                        self.output_text.insert(tk.END, f"下载章节: {title}\n")
                        self.output_text.update_idletasks()

                        # 更新下载进度文本
                        progress_text = f"下载进度: {idx + 1}/{total_chapters}"
                        self.progress_var.set(progress_text)
                        self.progress_label.update_idletasks()

            # 在下载函数结束后，重置下载进度文本
            self.progress_var.set("下载进度: 完成")

        with open(filename + book_name + '.txt', 'w', encoding='utf-8') as file:
            file.write(f"作者：{author}\n\n")
            file.write(result)

def main():
    root = tk.Tk()
    app = NovelDownloaderApp(root)

    # 设置窗口尺寸和位置
    window_width = 400
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # 设置窗口背景颜色
    root.configure(bg="#F0F0F0")

    # 设置图标
    icon = Image.open("icon.png")
    icon = icon.resize((32, 32), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(icon)
    root.iconphoto(False, icon)

    app.update_progress()
    root.mainloop()

if __name__ == "__main__":
    main()
