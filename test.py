import requests
# 为了防止发爬虫机制,用 requests 获取源代码
from pyquery import PyQuery as pq

# 用pq解析网页,拿取我们希望得到的元素

url = 'https://movie.douban.com/subject/24773958/reviews?start=20'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}


def get_html():
    # 接下来就是拿着这么多的URL 分别获取评论信息
    r = requests.get(url, headers=headers)  # 最大用时 142*500ms=9小时.....
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    doc = pq(html)
    content = doc('.short-content').text()
    print(content)

get_html()
