"""
1. selenium初识
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# # 声明浏览器对象
# browser = webdriver.Chrome()
#
# try:
#     # 使用get方法来请求网页
#     browser.get('https://www.baidu.com/')
#
#     # 查找搜索框的位置，通过查找网页源码定位搜索框节点
#     input1 = browser.find_element_by_id('kw')
#     input1.send_keys('python')
#     input1.send_keys(Keys.ENTER)
#
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
#
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)# 打印页面源代码
#
# finally:
#     browser.close()


"""
2. 查找单个节点

find_element_by_id()：根据节点id查找
find_element_by_name()：根据节点name值获取
find_element_by_class_name()：根据类名查找

find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_tag_name()

通用查找方法find_element():
find_element(By.ID, id) == find_element_by_id(id)
"""
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get('https://www.taobao.com/')
#
# input_one = browser.find_element_by_id('q')  # 所得结果均为WebEleement类型
# input_two = browser.find_element_by_name('q')
# input_three = browser.find_element_by_css_selector('#q')
# input_four = browser.find_element_by_xpath('//*[@id="q"]')
#
# print(input_one, '\n\n', input_two, '\n\n', input_three, '\n\n', input_four)
#
# browser.close()



"""
3. 查找多个节点

find_elements()
"""
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
#
# # 等价于lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# lists = browser.find_elements_by_css_selector('.service-bd li')
#
# print(lists)
#
# browser.close()


"""
4. 节点交互

send_keys()：输入文字
clear()：清空文字
"""
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
#
# browser = webdriver.Chrome()
#
# browser.get('https://www.taobao.com/')
#
# """
# input = browser.find_element_by_id('q')
# input.send_keys('Dell U2417h')
# input.send_keys(Keys.ENTER)# 按下Enter键
# """
#
# input1 = browser.find_element_by_id('q')
#
# input1.send_keys('iphone')
# time.sleep(1)
# input1.clear()
#
# input1.send_keys('ipad')
# button = browser.find_element_by_class_name('btn-search')
# # 鼠标点击
# button.click()


"""
5. 动作链

针对没有特定执行对象，如鼠标拖拽，键盘按键等。

实现节点的拖拽操作，将节点从一处拖至另一处
"""
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
#
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
#
# browser.switch_to.frame('iframeResult')
#
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
#
# actions = ActionChains(browser)  # 声明一个ActionChains对象
# actions.drag_and_drop(source, target)  # 将source拖拽至target
# actions.perform()  # 执行上述动作


"""
6. 执行JavaSceipt

对于Selenium API 没有提供的操作，比如下拉进度条，需要直接运行JavaScript，
使用execute_script()方法

注：JavaScript语句自己编写
"""
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')


"""
7. 获取节点信息

page_source属性获取网页源码，接着可以使用解析库来提取信息，
也可以使用Selenium返回的WebElement类型数据直接提取信息。

get_attribute()方法获取节点属性
text属性获取文本值
id属性获取节点id
location属性获取节点在页面中的相对位置
tag_name属性获取标签名称
size属性获取节点大小，即宽高
"""
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url = "https://www.zhihu.com/explore"
# browser.get(url)
#
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo, '\n\n')
# print(logo.get_attribute('data-za-a'), '\n\n')
#
# input1 = browser.find_element_by_class_name('zu-top-add-question')
# print(input1.text)
# print(input1.id)
# print(input1.location)
# print(input1.tag_name)
# print(input1.size)


"""
8. 切换Frame

网页中的有一种节点叫iframe，也就是子Frame，需要切换到该Frame
switch_to.frame()方法来切换
"""
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
#
# browser.switch_to.frame('iframeResult')
#
# # 首先直接查找类名为"logo"的节点
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No logo!')
#
# # 直接查找不到，切换到父节点
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
#
# print(logo)
# print(logo.text)


"""
9. 延时等待

get()方法在网页框架加载结束后结束执行，因此可能在获取的page_source并不是浏览器完全加载
完成的页面，若存在额外的Ajax请求则不能成功获取，因此需要延时等待确保节点加载出来。

等待方式：一是隐式等待；二是显式等待
"""


"""
隐式等待

若没有在DOM中找到节点将继续等待，超出设定时间后，则抛出找不到节点的异常，默认时间为0，
但是指定的是固定时间，效果不好，因为页面加载速度受网速影响。
"""
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
#
# # 隐式等待10秒
# browser.implicitly_wait(10)
# browser.get(url)
#
# input1 = browser.find_element_by_class_name('zu-top-add-question')
# print(input1)


"""
显式等待

指定要查找的节点，然后指定一个最长的等待时间，
在规定时间加载出来就返回节点，
规定时间没有加载出该节点则抛出超时异常。
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
#
# # 引入WebDriverWait对象，指定最长的等待时间
# wait = WebDriverWait(browser, 10)
#
# # 调用until()方法，传入等待条件，出现节点'q'
# # 10秒内如果ID为q的节点成功加载，则返回该节点，超过10秒没有加载出来就抛出异常
# # 等待条件还有很多，包括：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
# input1 = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
#
# print(input1, '\n\n', button)


"""
10. 前进和后退

forward()方法：前进一个页面
back()方法：后退一个页面
"""
# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.zhihu.com/')
#
# browser.back()
# time.sleep(5)
#
# browser.forward()


"""
11. Cookies

可以获取，添加，删除Cookies等。
"""
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
#
# print(browser.get_cookies())
#
# browser.add_cookie({'name':'name', 'domain':'www.zhihu.com', 'value':'germany'})
# print(browser.get_cookies())
#
# browser.delete_all_cookies()
# print(browser.get_cookies)


"""
12. 选项卡管理

可以对开启的多个选项卡进行操作
"""
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
#
# # 调用JavaScript语句window.open()另外开启一个选项卡
# browser.execute_script('window.open()')
# print(browser.window_handles)
#
# # 调用window_handles属性来切换选项卡，其中的参数是选项卡的代号。
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(5)
#
# browser.switch_to_window(browser.window_handles[0])


"""
13. 异常处理

使用try execept来捕获超时，节点未找到等异常，使程序即使出现错误也可以继续运行
"""
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import time
#
# browser = webdriver.Chrome()
#
# try:
#     browser.get('https://www.baidu.com/')
# except TimeoutException:
#     print('Time out.')
#
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No such element.')
# finally:
#     time.sleep(5)
#     browser.close()


"""
14. 爬取淘宝商品

用selenium抓取淘宝商品，用pyquery解析得到的商品图片，名称，价格，购买人数，店铺名称和店铺所在地信息，并将其保存至MongDB

未安装MongoDB，无法实现功能
"""
import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from config import *
from urllib.parse import quote

# browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input1 = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input1')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input1.clear()
            input1.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()
