#!-*-coding:utf-8-*-
# !@Date: 2018/12/26 22:34
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
12306购票思路:
利用selenium来模拟浏览器的行为, 重复发送请求, 购票
"""
import time
from selenium import webdriver

# 登录url
login_url = 'https://kyfw.12306.cn/otn/resources/login.html'

# 创建一个浏览器对象并打开登录页面
driver = webdriver.Chrome()
driver.get(login_url)

# 点击账号登录链接
login_href = driver.find_element_by_xpath('//li[@class="login-hd-account"]/a')
login_href.click()

# 输入账号和密码
account_box = driver.find_element_by_id('J-userName')
password_box = driver.find_element_by_id('J-password')

time.sleep(1)
account_box.send_keys('liu15671677014@sina.com')
time.sleep(1)
password_box.send_keys('tonyliu941103')

# 点击验证码
