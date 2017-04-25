# -*- coding: utf-8 -*-

# http://www.jianshu.com/p/b3bc88ffb251
__author__ = 'duohappy'

import requests
import re
from bs4 import BeautifulSoup

def re_test():
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    url = "http://tieba.baidu.com/f?kw=%E4%B8%BA%E7%9F%A5%E7%AC%94%E8%AE%B0"

    web_data = requests.get(url, headers=headers)

    # # 新知识点 web_data.content
    # # 以字节的方式访问web_data，所以用'wb'模式写入
    # with open('tieba_text.txt', 'wb') as f:
    #     f.write(web_data.content)
    web_data.encoding = 'utf-8'
    web_text = web_data.text
    # soup = BeautifulSoup(web_text, 'lxml')
    # with open('soup_text.txt', 'w') as f:
    #     f.write(str(soup))  # soup对象转成字符串

    reply_nums = re.findall(r'(?<="回复">)[\s\S]*?(?=</span>)', web_text)
    # reply_nums = re.findall(r'"回复">([\s\S]*?)</span>', web_text)
    # reply_nums = re.findall(r'("回复">([\s\S]*?)</span>)', web_text)

    print(reply_nums)

    url = "https://tieba.baidu.com/p/5054019406"
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'
    source_code = web_data.text
    # 匹配时间的正则
    time_pattern = r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}'
    # 匹配第一个时间
    create_time = re.search(time_pattern, source_code).group()
    print(create_time)

    # 匹配包含用户名正则表达式
    include_username_pattern = r'(?<=<li class="d_name"\sdata)[\s\S]*?(?=</a>)'
    # 匹配出来包含用户名的html代码
    include_username = re.search(include_username_pattern, source_code).group()
    # 匹配用户名的正则表达式
    username_pattern = r'(?<=target="_blank">)[\s\S]*'
    # First Time
    username = re.search(username_pattern, include_username).group()
    print(username)