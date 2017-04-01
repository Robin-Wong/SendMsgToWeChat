# -*- coding:utf-8 -*-

# http://www.jianshu.com/p/11d7da95c3ca

import requests  # 导入requests模块
from bs4 import BeautifulSoup  # 从bs4包中导入BeautifulSoup模块

# get weather html and parse to json
def get_weather(city_id):

    # 设置请求头
    # 更换一下爬虫的User-Agent，这是最常规的爬虫设置
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

    # 需要爬取的网址
    url = "http://www.weather.com.cn/weather1d/" + city_id + ".shtml"

    # 发送请求，获取的一个Response对象
    web_data = requests.get(url, headers=headers)

    # 设置web_data.text会采用web_data.encoding指定的编码，一般情况下不需要设置，requests会自动推断
    # 鉴于网页大部分都是采取utf-8编码的，所以设置一下，省去一些麻烦
    web_data.encoding = 'utf-8'
    # 得到网页源代码
    content = web_data.text

    # 使用lxml解析器来创建Soup对象
    soup = BeautifulSoup(content, 'lxml')

    # 为什么要创建一个Soup对象，还记得浏览器中的检查元素功能嘛
    # Soup对象可以方便和浏览器中检查元素看到的内容建立联系，下面会有动画演示
    # 使用css selector语法，获取白天和夜间温度，下面有动画演示
    city = soup.select('div.crumbs a')
    city2 = soup.select('div.crumbs span')
    tag_list = soup.select('p.tem span')

    # tag_list[0]是一个bs4.element.Tag对象
    # tag_list[0].text获得这个标签里的文本
    day_temp = tag_list[0].text
    night_temp = tag_list[1].text

    msg = ''
    for local in city:
        msg += local.text
        # print('{0} '.format(local.text), end='')
    for local in city2:
        if local.text != '>':
            msg += local.text
    msg += '\\n'
    # print()
    msg += '白天 {0}℃, 晚上 {1}℃'.format(day_temp, night_temp)
    # print('白天 {0}℃, 晚上 {1}℃'.format(day_temp, night_temp))
    # print(msg)

    return msg
