"""
1. 博主微博数据爬取

微博网址：https://m.weibo.cn/u/2830678474?uid=2830678474&luicode=10000011&lfid=1076032830678474

打开Ajax的XHL过滤器，可以看到Ajax数据请求
爬取博主的前十页微博
"""
# from urllib.parse import urlencode
# import requests
#
# from pyquery import PyQuery as pq
#
# base_url = 'https://m.weibo.cn/api/container/getIndex?'
#
# headers = {
# 	'Host': 'm.weibo.cn',
# 	'Referer': 'https://m.weibo.cn/u/2830678474?uid=2830678474&luicode=10000011&lfid=1076032830678474',
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
# 	'X-Requested-With': 'XMLHttpRequest'
# }
#
#
# # 获取页面
# def get_page(page):
# 	# 定义url参数字典
# 	params = {
# 		'type': 'uid',
# 		'value': '2830678474',
# 		'containerid': '1076032830678474',
# 		'page': page
# 	}
# 	# 获取请求url
# 	url = base_url + urlencode(params)
# 	try:
# 		# 获取页面响应
# 		response = requests.get(url, headers=headers)
# 		# 若响应正常，通过json()方法将内容解析为JSON返回
# 		if response.status_code == 200:
# 			return response.json()
# 	# 若出现异常则捕获异常信息返回
# 	except requests.ConnectionError as e:
# 		print('error!', e.args)
#
#
# # 解析页面，传入JSON对象
# def page_parse(json):
# 	# 若传入JSON对象
# 	if json:
# 		# 希望获取内容为data标签下的cards标签下
# 		items = json.get('data').get('cards')
# 		# 希望获取保存微博id，正文，赞数，评论数，转发数几个内容，因此遍历cards，
# 		# 得到cards标签下的mblog中的信息
# 		for item in items:
# 			item = item.get('mblog')
# 			weibo = {}
# 			weibo['id'] = item.get('id')
# 			weibo['text'] = pq(item.get('text')).text()
# 			weibo['attitudes'] = item.get('attitudes_count')
# 			weibo['comments'] = item.get('comments_count')
# 			weibo['data'] = pq(item.get('created_at')).text()
# 			weibo['reposts'] = item.get('repost_count')
# 			yield weibo
#
#
# # 遍历page，提取输出的结果并打印
# if __name__ == '__main__':
# 	weibo_number = 0
# 	for page in range(1, 80):
# 		json = get_page(page)
# 		results = page_parse(json)
# 		for result in results:
# 			print(result)
# 			weibo_number += 1
# 	print('weibo_number:', weibo_number)


"""
2. 博主'冬天的橡树暖暖的'微博爬取

博主首页地址：https://weibo.com/u/3930508963?topnav=1&wvr=6&topsug=1&is_all=1
"""


"""
3. 今日头条街拍美图爬取
"""
# import requests
# import urllib
# import os
# from hashlib import md5
# from multiprocessing.pool import Pool
#
#
# def get_page(offset):
# 	params = {
# 		'offset': offset,
# 		'format': 'json',
# 		'keyword': '街拍',
# 		'autoload': 'true',
# 		'count': '20',
# 		'cur_tab': '1'
# 	}
#
# 	url = 'https://www.toutiao.com/search_content/?' + urllib.parse.urlencode(params)
#
# 	headers = {
# 		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# 	}
#
# 	try:
# 		response = requests.get(url, headers=headers)
# 		if response.status_code == 200:
# 			return response.json()
# 	except response.ConnectionError as response_error:
# 		return ('error!', response_error.args)
#
#
# def get_images(json):
# 	if json.get('data'):
# 		for item in json.get('data'):
# 			title = item.get('title')
# 			images = item.get('image_list')
#
# 			for image in images:
# 				yield {
# 					'image': image.get('url'),
# 					'title': title
# 				}
#
#
# def save_images(item):
# 	if not os.path.exists(item.get('title')):
# 		os.mkdir(item.get('title'))
#
# 	try:
# 		response = requests.get(item.get('image'))
# 		if response.status_code == 200:
# 			file_name = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
# 			if not os.path.exists(file_name):
# 				with open(file_name, 'wb') as f:
# 					f.write(response.content)
# 			else:
# 				print('Already downloaded.', file_name)
# 	except requests.ConnectionError as e:
# 		print('Failed to save image.', e.args)
#
#
# def main(offset):
# 	json = get_page(offset)
# 	for item in get_images(json):
# 		print(item)
# 		save_images(item)
#
#
# GROUP_START = 1
# GROUP_END = 80
#
# if __name__ == '__main__':
# 	pool = Pool()
# 	groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
# 	pool.map(main, groups)
# 	pool.close()
# 	pool.join()

# import os
# import requests
# from urllib.parse import urlencode
# from hashlib import md5
# from multiprocessing.pool import Pool
#
# GROUP_START = 1
# GROUP_END = 2
#
#
# def get_page(offset):
# 	params = {
# 		'offset': offset,
# 		'format': 'json',
# 		'keyword': '街拍',
# 		'autoload': 'true',
# 		'count': '20',
# 		'cur_tab': '3',
# 		'from': 'gallery',
# 	}
# 	url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
# 	try:
# 		response = requests.get(url)
# 		if response.status_code == 200:
# 			return response.json()
# 	except requests.ConnectionError:
# 		return None
#
#
# def get_images(json):
# 	data = json.get('data')
# 	if data:
# 		for item in data:
# 			# print(item)
# 			image_list = item.get('image_list')
# 			title = item.get('title')
# 			# print(image_list)
# 			for image in image_list:
# 				yield {
# 					'image': image.get('url'),
# 					'title': title
# 				}
#
#
# def save_image(item):
# 	if not os.path.exists(item.get('title')):
# 		os.mkdir(item.get('title').rstrip('?'))
# 	try:
# 		response = requests.get('http:' + item.get('image'))
# 		if response.status_code == 200:
# 			file_name = '{0}/{1}.{2}'.format(item.get('title').rstrip('?'), md5(response.content).hexdigest(), 'jpg')
# 			if not os.path.exists(file_name):
# 				with open(file_name, 'wb')as f:
# 					f.write(response.content)
# 			else:
# 				print('Already Downloaded', file_name)
# 	except requests.ConnectionError:
# 		print('Failed to save image')
#
#
# def main(offset):
# 	json = get_page(offset)
# 	for item in get_images(json):
# 		print(item)
# 		save_image(item)
#
#
# if __name__ == '__main__':
# 	pool = Pool()
# 	groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
# 	pool.map(main, groups)
# 	pool.close()
# 	pool.join()
