import os
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def crawl_luogu(difficulty, keywords):
    # 构造请求头部信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # 发送GET请求获取洛谷题目列表页的内容
    url = 'https://www.luogu.com.cn/problem/list?difficulty={}&keyword={}'.format(difficulty, keywords)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取题目列表
        problem_list = soup.find_all('div', class_='lg-list-item')
        for problem in problem_list:
            # 获取题目编号
            problem_id = problem.find('a', class_='lg-list-item-tag').string
            # 获取题目标题
            problem_title = problem.find('a', class_='lg-list-item-title').string

            # 创建题目文件夹
            folder_name = '{}-{}'.format(problem_id, problem_title)
            folder_path = os.path.join(difficulty, keywords, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            # 爬取题目内容
            problem_url = 'https://www.luogu.com.cn/problem/{}'.format(problem_id)
            problem_response = requests.get(problem_url, headers=headers)
            problem_soup = BeautifulSoup(problem_response.text, 'html.parser')
            # 获取题目内容
            problem_content = problem_soup.find('div', class_='lg-article').text.strip()
            # 将题目内容保存为markdown文件
            problem_file_path = os.path.join(folder_path, '{}-{}.md'.format(problem_id, problem_title))
            with open(problem_file_path, 'w', encoding='utf-8') as file:
                file.write(problem_content)

        else:
            messagebox.showerror('Error', 'Failed to crawl Luogu problems.')

        # 创建GUI页面
        root = Tk()
        root.title('Luogu Crawler')
        root.geometry('300x200')

        # 难度选择菜单
        difficulty_label = Label(root, text='Difficulty:')
        difficulty_label.pack()
        difficulty_var = StringVar(root)
        difficulty_var.set('all')
        difficulty_menu = OptionMenu(root, difficulty_var, 'all', '0', '1', '2', '3', '4', '5')
        difficulty_menu.pack()

        # 关键词输入框
        keywords_label = Label(root, text='Keywords:')
        keywords_label.pack()
        keywords_entry = Entry(root)
        keywords_entry.pack()

        # 开始爬取按钮
        crawl_button = Button(root, text='Crawl',
                              command=lambda: crawl_luogu(difficulty_var.get(), keywords_entry.get()))
        crawl_button.pack()

        root.mainloop()

