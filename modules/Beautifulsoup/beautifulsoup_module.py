"""
1. 基本用法
"""
# from bs4 import BeautifulSoup
#
# # 不完整的HTML字符串（部分节点未闭合）
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html, 'lxml')  # 解析html，完成BeautifulSoup对象初始化，此时可将html自动更正格式
#
# print(soup.prettify())  # prettiffy()方法将需解析的字符串以标准的缩进格式输出
#
# print(soup.title.string)  # 输出title节点的文本内容


"""
2. 节点选择器

直接调用节点的名称，在调用string属性即可得到节点内的文本
"""
# from bs4 import BeautifulSoup
#
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
#
# html2 = """
# <html>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             Hello
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
# """
#
# soup = BeautifulSoup(html, 'lxml')
# soup2 = BeautifulSoup(html2, 'lxml')
#
# print(soup.title)
# print(type(soup.title), '\n')  # <class 'bs4.element.Tag'>，即Tag类型
#
# print(soup.head, '\n')
#
# # 当有多个节点时，此种方式只会匹配第一个匹配的节点
# print(soup.p, '\n')
#
# # 获取节点属性的名称
# print(soup.title.name, '\n')
#
# # 获取节点属性
# print(soup.p.attrs)  # 字典形式
# print(soup.p.attrs['name'], '\n')  # 节点具有多个属性，只获取'name'属性
#
# # 嵌套选择
# # Tag类型基础上再次选择仍然是Tag类型
# print(soup.head.title.string, '\n')
#
# # 关联选择
# # 获取节点元素的直接子节点，直接调用contents属性，返回的为列表形式
# print(soup.p.contents, '\n')
#
# # 获取某个节点元素的父节点，调用parent/parents属性
# print(soup.a.parent, '\n')  # a的直接父节点
# print(soup.a.parents, '\n')
#
# # 获取兄弟节点（同级节点）
# print(soup2.a.next_sibling)
# print(list(enumerate(soup2.a.next_siblings)), '\n\n\n')
#
# print(soup2.a.previous_sibling)
# print(list(enumerate(soup2.a.previous_siblings)), '\n')


"""
3. 方法选择器（建议使用用来匹配结果）

find_all()和find()，更灵活的查询选择，API如下：
find_all(name , attrs , recursive , text , **kwargs)

find()返回的为单个元素，即第一个匹配的元素

其他查询方法find_parents()，find_next_siblings()等可参照
"""
# from bs4 import BeautifulSoup
#
# html = """
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo, hello, this is link1</li>
#             <li class="element">Bar, this is link2</li>
#             <li class="element">Jay, this is link3</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# """
#
# soup = BeautifulSoup(html, 'lxml')
#
# # name：直接通过节点名称找出所有ul节点
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]), '\n\n')  # Tag形式
#
# # 查询出所有的ul节点之后，继续查询内部的li节点
# for ul in soup.find_all(name='ul'):
#     print(soup.find_all(name='li'))
#     for li in ul.find_all(name='li'):  # 遍历li节点，获取其文本
#         print(li.string)
#
# # attrs：通过节点的属性找到节点
# print('\n\n')
# print(soup.find_all(attrs={'id': 'list-2'}), '\n')
# print(soup.find_all(attrs={'class': 'list list-small'}))
#
# # 对于常用的属性如id和class(关键字，后加下划线)等不需attrs传递，可直接传入参数
# print('\n\n')
# print(soup.find_all(id='list-1'), '\n')
# print(soup.find_all(class_='element')[0].string)
#
# # text：匹配节点文本，传入形式为字符串或正则表达式对象
# print('\n\n')
# import re
# print(soup.find_all(text=re.compile('link1')))  # 将link1编译为正则表达式对象


"""
4. CSS(层叠样式表)选择器

参考网址：http://www.w3school.com.cn/css/css_jianjie.asp

直接调用select()方法，传入相应的CSS选择器即可
"""
# from bs4 import BeautifulSoup
#
# html = """
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# """
#
# soup = BeautifulSoup(html, 'lxml')
#
# print(soup.select('.panel .panel-heading'), '\n')
# print(soup.select('ul li'), '\n')
# print(soup.select('#list-2 .element'), '\n')
#
# print(type(soup.select('ul')[0]), '\n')# 仍为Tag类型，可使用嵌套
#
# for ul in soup.select('ul'):
#     print(ul.select('li'))
#     print(ul['id'], ul['class'])
#
# # 获取文本，除了string属性，还有一个方法get_text()，结果输出相同
# print('\n\n')
# for li in soup.select('li'):
#     print('Get Text:', li.get_text())
#     print('String:', li.string)
