#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import json
import os
import re
import time

import emoji
import pandas
import requests

# 爬取并处理50页
start_page = 1
end_page = 51


class TmallCommentSpider(object):

    def __init__(self, item_id, base_url):
        """item_id作为保存文件夹的名称"""
        # base_url的页码需要被替换，有追评的,append参数为1
        self.item_id = item_id
        self.base_url = base_url
        self.headers = {
            "authority": "rate.tmall.com",
            "method": "GET",
            # "path": "/list_detail_rate.htm?itemId=558862700835&spuId=877095771&sellerId=1776456424&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvhpvRvpWvUpCkvvvvvjiPRs5OljtPPLdyAjthPmPhgjinnLd9zjDvnLMOsjYRPFyCvvpvvvvvdphvmpvUJINxlpm%2BVu6Cvvyvm2KVh1WvJjQCvpvVvvpvvhCvKphv8vvvvvCvpvvvvvvCoZCv2V9vvvWvphvW9pvvvQCvpvACvvv2vhCv2UVEvpvVmvvC9jaPuphvmvvv92JwQZ2lmphvLvQphvvjw%2Bet9E7rejh%2BYExrt8TxEcqhQj7Q%2BultEPoUaO97%2B3%2BuQjc6D40OwoA%2BD7zyd3ODNKBlYE7rV169YExr1CkKfvDr6jc6%2Bu6Pvpvhvvvvv2yCvvpvvvvviQhvCvvv9U8jvpvhvvpvv86Cvvyv2mTjEAwvibeCvpvZ7DAcZRMw7Di43MM5MREwVHiMz1h%3D&needFold=0&_ksTS=1575655128672_1490&callback=jsonp1491",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "enc=GA7n2hldx4qYCGyz22P8HwUL53T0LflICbWOi%2FUpHZtGpAg3r6dt66OQxxd6Xm14RsviZKdKRA97Cjqy5WJv2w%3D%3D; cna=eegCFMPhoWUCARsmOBr1I683; dnk=tb91997919; tracknick=tb91997919; lid=tb91997919; lgc=tb91997919; login=true; cookie2=159cb9d08e483334c0d092baf188998e; t=193666644cf9583355cf28275eaceb31; _tb_token_=fe583e317d5a3; JSESSIONID=967825BBB84F72576C16403DDF5CFFCC; hng=CN%7Czh-CN%7CCNY%7C156; uc1=pas=0&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&existShop=false&cookie14=UoTbmE0q%2FB5Bug%3D%3D&lng=zh_CN&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D; uc3=vt3=F8dByus%2B2Z1AlemIrBY%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&nk2=F5RMGL%2BCibGQ0w%3D%3D&id2=UonfNiTL1Dc11Q%3D%3D; _l_g_=Ug%3D%3D; uc4=nk4=0%40FY4HXZa45pGuQdHGbtDXwhPUmota&id4=0%40UOE1hWW77syyE8mtA%2F22tUL%2BCe6i; unb=1841055639; cookie1=W816IKqvrPTY%2B7YUzpT9ZeWNu0LWql23ib874oOj1KE%3D; cookie17=UonfNiTL1Dc11Q%3D%3D; _nk_=tb91997919; sg=997; csg=cf30b543; _m_h5_tk=c4e52f189378737ca8ccc1fb682ea488_1575671396518; _m_h5_tk_enc=0092d7e7913cedc5c66104afbded6d1f; x5sec=7b22726174656d616e616765723b32223a2238343435363132313166313130393234663339383661613037353539383434364349666571753846455032417a756536313754664f426f4d4d5467304d5441314e54597a4f547378227d; l=dBId3bK7vaip7zSXBOfgNuI8Ls7OXIOfGsPzw4OGjICPOnCVhFPAWZKaNGLyCnGVn6kpJ3Jt3efYBlYnVyznhZXRFJXn9MpONdTh.; isg=BGpq0C0pw8-_6klE1Y5pDrxpu9DMc-9dRZW-tvQiaL18Jw7h3WoqRHMRtxOe12bN",
            "referer": "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.3e911200p7QB4e&id=558760911386&skuId=3475266621309&areaId=440300&user_id=2616970884&cat_id=2&is_b=1&rn=42b69425afb62e3b57164036c3b9c667",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
    
    def get_content(self, current_page):
        """
        获取所有内容
        :return: str
        """
        request_url = self.base_url.format(current_page)
        print("正在请求：", request_url)
        content = requests.get(request_url, headers=self.headers, timeout=15).content.decode("utf-8")
        # TODO: 将content的首尾的不必要字符去掉
        return content
    
    def save_content(self, file_path, content):
        """保存所有内容至文件"""
        print("正在保存数据至文件:", file_path)
        with open(file_path, "w") as f:
            f.write(content)

    def save_comments(self):
        """保存评论至本地"""
        file_path = "./comments/{}".format(self.item_id)
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        for i in range(start_page, end_page):
            content = self.get_content(i)
            # TODO:适当降低爬取速度
            time.sleep(0.2)
            file_full_path = os.path.join(file_path, "tmall_comment{}.txt".format(i))
            self.save_content(file_full_path, content)


def get_comments(file_path, start_page=1, end_page=51):
    """
    从单个item中的所有文件中取得评论信息
    :param file_path: str,评论文件的路径
    :param start_page: int
    :param end_page: int
    :return: list
    """
    print("正在提取的评论来自:", file_path)
    comments = []
    for i in range(start_page, end_page):
        file_full_path = os.path.join(file_path, "tmall_comment{}.txt".format(i))
        with open(file_full_path, "r") as f:
            content = f.read()
        # 去除字符中的emoji表情
        content = emoji.demojize(content)
        # TODO: 需要完善转换过程
        content_dict = json.loads(content[11:-1])

        # 每个文件保存20条信息
        for j in range(20):
            rate = content_dict["rateDetail"]["rateList"][j]  # 单条评论的所有信息

            rate_content = rate["rateContent"]  # 评论内容
            rate_date = rate["rateDate"]  # 评论日期
            auction_sku = rate["auctionSku"]  # 机型
            display_user_nick = rate["displayUserNick"]  # 用户昵称

            append_comment = rate["appendComment"]  # 追评
            append_comment_content = append_comment["content"]  # 追评内容
            append_comment_time = append_comment["commentTime"]  # 追评时间

            comments.append({
                "用户名": display_user_nick,
                "当天评论": rate_content,
                "当天日期": rate_date,
                "机型": auction_sku,
                "追加评论": append_comment_content,
                "追加评论日期": append_comment_time
            })
    return comments


def save_to_csv():
    """
    将单个item评论格式化至csv格式
    """
    save_path = "./csvs"
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    # TODO：取得所有文件夹路径
    item_dirs = os.listdir("./comments")

    for item_dir in item_dirs:
        file_path = os.path.join("./comments", item_dir)
        comments = get_comments(file_path)
        
        # 将数据保存至csv文件
        df_data = pandas.DataFrame(comments)
        
        save_dir = os.path.join("./csvs/{}".format(item_dir))
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        
        save_full_path = os.path.join(save_dir, "{}.csv".format(item_dir))
        print("保存评论csv至:", save_full_path)
        df_data.to_csv(save_full_path, encoding="utf_8_sig")


if __name__ == "__main__":

    # phones =[
        # {
        #     "name": "iphone8",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=558760911386&spuId=877095771&sellerId=2616970884&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvvpvnvRgvUvCkvvvvvjiPRs5O0jiER2dhsjYHPmPytjlURss91jtRP2FhzjlRRphvCvvvvvmCvpvWz%2FaJ5WD4zYMNWUzwdphvmpvhF9WkU9vy6gwCvvpvCvvv2QhvCvvvMMGEvpCWmVt%2Bvva4afmDYb8rwZnlMWFZVi1TowFp6bvqrADn9W2%2BFfmtEpcWTWexRdIAcUmxfaAK5FaJKXVYz40AVArlafmxdB9aUneYiXhpV8yCvv9vvUvz5mC6cOyCvvOUvvVva6%2FtvpvIvvvv9hCvVvpvvUCephvwtvvvv31vpCQmvvvmjhCvjvUvvvUfphvw%2FphCvvOvCvvvphvtvpvhvvvvv8wCvvpvvUmmdphvmpvhVvPo69v9mv%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575661349311_1273&callback=jsonp1274",
        #     "item_id": "558760911386"
        # },
        # {
        #     "name": "huawei mate 30 pro",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=603330883901&spuId=1351702554&sellerId=2838892713&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvHpvnvPOvUvCkvvvvvjiPRs5wQjtEPLLyljivPmPh1jn2P2LhljlHnL5ZgjDb9phvHnQGwjVHzYswzRC87MJvPjMwOHuCdphvmpmCwVwbvvv8HUwCvvpv9hCviQhvCvvvpZpPvpvhvv2MMQhCvvOvChCvvvvEvpCWvSHX7BzZeief5jXh1nmODC40f3qxsLpZVXB%2BvfFCKdy6HjEf%2BE7re8TJfxAQABoXH3D%2Bm7zhdip7%2B3%2BuaNo0HskzWCky%2Bb8rV4tYVbyCvm9vvhCCvvv29vvvBjUvvUVyvvChNvvv96vvvhBGvvm2pvvvBjUvvUWMuphvmvvvpoYM3B3ZkphvC9hvpyPwg2yCvvpvvhCvdphvmpmC7hM8vvmPWsyCvvpvvhCv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575705727614_1899&callback=jsonp1900",
        #     "item_id": "603330883901"
        # },
        # {
        #     "name": "honnor 9x",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=598079959720&spuId=1260500122&sellerId=1114511827&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvfQvnvPOvUpCkvvvvvjiPRs5wQjtjRFLOzjEUPmPv0jDRP2FO6j1hRLzwQjlWRLyCvvpvvhCv3QhvCvmvphm5vpvhvvCCB2yCvvpvvhCv2QhvCvvvvvmivpvUvvCCbz%2FxvCoEvpvVvpCmpYs9Kphv8vvvphhvvvRvvvChw9vv94pvvhBGvvm2pvvvBjQvvUnvvvChw9vv9sGEvpCW9o48k3z6%2Bu0OeC6sF4VQR4VzEhhH6BoAdX3sbuoQ%2Bu0OjC69D70OVTgNN3rr1EKKHdUf8wBl5d8rejOdGPmAdXkwjLVxfX9fdigDN9hCvvOvChCvvvmrvpvEvvjIG79vvUz1dphvmpmC7yU2vvvPOIhCvCB4cJmODn147DitN%2FwGNDsK75qNhp%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575705977084_1984&callback=jsonp1985",
        #     "item_id": "598079959720"
        # },
        # {
        #     "name": "vivo z5x",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=594381462179&spuId=1221849181&sellerId=883737303&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvLpvpvB6vjQCkvvvvvjiPRs5wQjlnnLzU6j1VPmPOAjrURFMpljYER2qyQjytvpvhvvCvpUhCvCLwPjrAonMwznAe6HSz9PslzVC4946CvvyvvJPqfpvv8Be5vpvhvvCCBvGCvvpvvvvvvphvC9vhphvvvvyCvhQvVTuujwma%2BfmtEpcWT2eARdIAcUmxdBeK5kHTD76wdug78BoxfBeK51rgpwFIViefHFXXiXhpVE01Ux8x9CIaRfU6pwethb8rVC60Kphv8vvvphhvvvRvvvChw9vv94pvvhBGvvm2pvvvBjQvvUnvvvChw9vv9s%2FivpvUvvCCbz%2FXfzkEvpvVvpCmpYs9RphvCvvvphmjvpvhvUCvp86CvvyvvVisSvvvUnmrvpvEvvViSSgvvmxhdphvmpmC7Zqdvvveh86Cvvyv9xCUkvvvuaw%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575706113606_1899&callback=jsonp1900",
        #     "item_id": "594381462179"
        # },
        # {
        #     "name": "xiaomi note8",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=600630289146&spuId=1324378865&sellerId=1714128138&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvBQvWvPhvUvCkvvvvvjiPRs5wQjlPPLs9sjD2PmPwtjiRRLsU1j1WRsqysj1RRphvChCvvvmrvpvBohkscW%2BvpV8dgclBnf%2BAZsvtvpvhphvvvvhCvvXvovvvvvmivpvUphvhKJG6GKREvpvVpyUUCE%2BwKphv8hCvvvpvvhXjphvp0vvvpQivpC29vvCj16CvhRvvvhNjphvp0vvvBsyEvpCWpLcUv8RJEctz8dmxdX%2BaUVEv%2BE7rV369wHADYEyfwyx%2BVd0DW3CQoAnmsXZpejEUWDNBlLyzOvZfU5c6%2Bul687gnIOZtIoYbE7LBIvGCvvpvvPMMiQhvChCvCCojvpvhphhvvUhCvCLwPUE1VrMwzns3HxSz9CABzVC49p%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575706221479_3032&callback=jsonp3033",
        #     "item_id": "600630289146"
        # },
        # {
        #     "name": "honnr 20",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=594370342052&spuId=1222231185&sellerId=1114511827&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvFQvnvPOvUvCkvvvvvjiPRs5wQjlRPFL96jrCPmPZQjiRPsFw6jnHPsMhgjrR9phvHnQG3jjazYswzUmo7MJvj8zwOHuCdphvmpvWHgSMMQmWhT6CvvyvCjebdugv9URjvpvhvvpvvvGCvvpvvPMMmphvLvm7fpvjwYcEKOmAdcwuYU31lBkOa1H1lw2hVdhw4w2h6U6KK5CClED1lBkOahRU%2BExreutYcgkQD764d5ln%2B8c61Ey4ahmQ0f0DW3mtvpvIvvvv9hCvVvpvvvUfphvWEpvvv31vpCQmvvvmjhCvjvUvvvUfphvw%2FOyCvvOUvvVva6%2FivpvUvvmvntMlMovCvpvVvmvvvhCvRphvCvvvvvm5vpvhvvmv9FyCvvpvvvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575706338589_2651&callback=jsonp2652",
        #     "item_id": "594370342052"
        # },
        # {
        #     "name": "oppo k3",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=593529520193&spuId=1215274749&sellerId=901409638&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvkpvWvRyvUvCkvvvvvjiPRs5wQjlUPLMygjEUPmP91jinPLcWgjiURFFhQj1EdphvmpvCKuE8vvvpDIwCvvpv9hCviQhvCvvvpZpPvpvhvv2MMQhCvvOvChCvvvmtvpvIvvCvppvvvgvvvhBAvvmCivvvBjQvvUnvvvChNvvv96vvvhBAvvm2PTyCvv9vvhhSNqZiUgyCvvOCvhE2zRvEvpCW9NV1%2BBzhe8TJuLBVifesHsWtb6UnIfvtIfwyp4mxdXkfdeDHD70wdiTAVAEldb8reE9aW4c65C%2BOHFXXiXhpVbT%2F4vJQKXwXVFtQ7LyCvvpvvhCv9phvHnQGNjU8zYswzVCH7MJvjnswOHuCRphvCvvvphv%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575706523661_1994&callback=jsonp1995",
        #     "item_id": "593529520193"
        # },
        # {
        #     "name": "huawei nova5 pro",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=596201072920&spuId=1247033188&sellerId=2838892713&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvupvpvBpvUvCkvvvvvjiPRs5wQjlbPLSy1jD2PmP91jrURFqUljnjPscp6jr2RphvChCvvvvjvpvjzn147rG9iFyCvvBvpvvvRphvChCvvvvPvpvhvv2MMTyCvv3vpvotqsJIyUyCvvXmp99he1AtvpvIphvvCvvvByavpC2OvvCjNyCvhRvvvhNjphvpgvvvBGavpC2OvvCjRpyCvh1CMcWvIqIAcVvHfaoKD7rj8BLO1EKXfCISBiVvVE6FpFn79WkOjLEcnhjEKBmAVAi08MoxdX3080r4%2B87JejHhJZTQ0fJ6EvBQog0HvphvCyCCvvvvv8wCvvBvpvpZ3QhvChCCvvmCvpvWzCA7ORFNznswPUt4RphvChCvvvmrvpvEphWBcEyvpVqQ9phvHnQG3cHEzYswzRbi7MJvjjFwOHuC&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575706630578_1627&callback=jsonp1628",
        #     "item_id": "596201072920"
        # },
        # {
        #     "name": "huawei p30",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=589814336859&spuId=1184907650&sellerId=2838892713&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvfvvRvByvUpCkvvvvvjiPRs5wQjl8RLqw6j1VPmPplji8n2FwAjiEn2q90j38RIhCvCLNYAV%2FjldNzYMv%2FS1afYM7zMFwQ86CvvDvpdn9D9Cv7Dwtvpvhphvvv8wCvvBvpvpZRphvChCvvvvCvpvVphhvvvvvKphv8hCvvvpvvhXjphvp0vvvBztvpC29vvCj16CvhRvvvhNjphvp0vvvBseivpvUphvhKJGgrDuEvpvVpyUUCE%2BwmphvLhW7wvmFr2Bc8vmYib01UxUDCw2IRfU6pLEw9E7re169wx0DYEufJhY%2BVd0DW3CQoAnmsXZpejIUExjxALwpEctl8PoxdXIaneUjFahPvpvhvvvvvUwCvvBvppvvCQhvEW2Nzn14OWQu6eIU4d%2F1Uz%2BfgJduSGFTOOVB9%2B88yEHtycy2OFyCvvBvpvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575706760630_1873&callback=jsonp1874",
        #     "item_id": "589814336859"
        # },
        # {
        #     "name": "huawei changxiang10 plus",
        #     "base_url": "https://rate.tmall.com/list_detail_rate.htm?itemId=601249956166&spuId=1329513962&sellerId=2838892713&order=3&currentPage={}&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvW9vpvBpvUvCkvvvvvjiPRs5wQjlhR2Lv1jthPmPy0jDPR25v1jtVP2cvtjDWRphvCvvvphmCvpvWzPAtcNqNznswjR143QhvCvmvphvCvpvVvUCvpvvvkphvC9hvpyPwg8yCvv9vvhhSNGzglqyCvm9vvhCCvvv29vvvBjUvvURwvvChNvvv96vvvhBGvvm2pvvvBjUvvUWMmphvLvbZ8oyaz8g7%2Bul1bPLhHdoJecHVQbvqrqpAOH2%2BFfmt%2B3C1BKFE%2BFuTRogRD70fdiT1VAtl%2BboJeEDsBYkQRqJ6WeCpqU0QKfUpwZyPvpvhvv2MMsyCvvpvvhCviQhvCvvvpZpjvpvjzn147rGUELyCvvpvvhCvdphvmpmvkOVrvvmjLghCvCLwPjXSdrMwznANklSz9Cs8zVC49LyCvvpvvhCv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1575706955969_1848&callback=jsonp1849",
        #     "item_id": "601249956166"
        # },
    # ]

    # 爬取所有的评论内容并保存
    # for phone in phones:
        # tmall_spider = TmallCommentSpider(phone["item_id"], phone["base_url"])
        # tmall_spider.save_comments()

    # 提取有用的评论内容并保存至csv
    save_to_csv()
