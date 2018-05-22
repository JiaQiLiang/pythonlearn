import requests
# 为了防止发爬虫机制,用 requests 获取源代码
from pyquery import PyQuery as pq

# 用pq解析网页,拿取我们希望得到的元素

from bs4 import BeautifulSoup as bs

import random

"""
https://movie.douban.com/subject/24773958/reviews?start= 
 注意 start 0  20    40    60    80 分别代表第二页 第三页 第四页
            0  1*20 2*20  3*20  4*20
"""

baseUrl = 'https://movie.douban.com/subject/24773958/reviews?start='
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}


def get_html():
    for i in range(1):  # 一共显示了142页,先输出两页的
        url = baseUrl + str(i * 20)
        # 接下来就是拿着这么多的URL 分别获取评论信息
        random_num = random.randrange(200, 500)  # 随机访问网址获取网页
        r = requests.get(url, headers=headers, timeout=random_num)  # 最大用时 142*500ms=9小时.....
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = bs(r.text, 'lxml')
        atab = soup.find_all(attrs={"class": "reply"})  # 输出结果是ResultSet
        for item in atab:
            href = item.attrs['href']

            cut = href[32:39]  # 成功输出字符,下一步开始抓取数据


get_html()
