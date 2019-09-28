"""
coding = UTF-8

抓取猫眼电影Top100榜单的电影信息，提取的信息包括：
排名
片名
海报
评分
主演
发布时间

抓取的站点：http://maoyan.com/board/4

offset = 10
"""
# 单一一项的内容如下：
r'''
 <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click" data-val="{movieId:1297}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/__40191813__4767047.jpg@160w_220h_1e_1c" alt="肖申克的救赎" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
        <p class="star">
                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
        </p>
<p class="releasetime">上映时间：1994-10-14(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>



需要提取内容顺序依次为：
1. 排名（2）
2. 片名（肖申克的救赎）
3. 海报图片（<img data-src="http://p0.meituan.net/movie/__40191813__4767047.jpg@160w_220h_1e_1c" alt="肖申克的救赎" class="board-img" />）
4. 主演（主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿）
5. 上映时间（1994-10-14（美国））
6. 评分（9.5）

对应的提取正则表达式：
<dd>.*?board-index-2">(.*?)</i>.*?title="(.*?)".*?<img\sdata-src="(.*?)".*?<p\sclass="star">.*?(主演.*?).*?</p>.*?(上映时间.*?)</p>.*?class="integer">(\d+)</i><i class="fraction">(\d+)</i></p>.*?<dd>
'''

import requests
import re
import json
import time
from requests.exceptions import RequestException


# 首先抓起第一页的内容，传入抓取地址url，将抓取页面内容返回
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        response = requests.get(url, headers=headers)

        # 若响应正常，返回文本，否则不返回
        if response.status_code == 200:
            return response.text
        return None

    except RequestException:
        return None


# 解析单个页面
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
        + '(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?'
        + 'integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)

    # 得到的items是个元素为tuple的list，为当前页10项电影的信息
    items = re.findall(pattern, html)

    # 将匹配结果items遍历提取结果，并生成字典形式
    for item in items:
        '''
        带有该yield关键字的函数不是普通函数，而是一个生成器（generator），用于迭代
        简要理解：yield就是 return, 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始；
        可参考网址：https://www.cnblogs.com/cotyb/p/5260032.html
        '''
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],  # strip()[3:]表示跳过item[3]的前三个字符
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
    print(items)


# 写入文件，将字典写入到文本文件
def write_to_json(content):
    with open('maoyan_top100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# 因为我们需要抓取的是TOP100的电影，所以还需要遍历一下，给这个链接传入offset参数
# 实现其他90部电影的爬取
# main()函数一次实现一页处理
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)

    for item in parse_one_page(html):
        # print(item)
        write_to_json(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)  # 睡眠1秒，用于防止反爬
