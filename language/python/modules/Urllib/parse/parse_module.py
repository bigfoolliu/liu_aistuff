'''
1. urlparse()

该方法可实现URL的识别和分类
'''
'''
import urllib.parse, urllib.request

result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')

print(type(result), result, sep='\n')
'''
''' 
urlparse()方法将其拆分成了6部分:
对应标准的链接格式如：scheme://netloc/path;parameters?query#fragment
'''

'''
2. urlunparse()

可实现URL的构造，接受的参数是一个可迭代对象，但是它的长度必须是6，否则会抛出参数数量
不足或者过多的问题
'''
'''
from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']

print(urlunparse(data))
'''

'''
3. urlsplit()

该方法类似于urlparse()，但只返回5个参数，params会合并到path中
'''
'''
from urllib.parse import urlsplit
 
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result.scheme, result[2])
'''

'''
4. urlunsplit()

与urlunparse()类似，它也是将链接各个部分组合成完整链接的方法，传入的参数也是一个
可迭代对象，例如列表、元组等，唯一的区别是长度必须为5。
'''
'''
from urllib.parse import urlunsplit
 
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
'''

'''
5. urljoin()

生成链接还有另一个方法，那就是urljoin()方法。我们可以提供一个base_url（基础链接）
作为第一个参数，将新的链接作为第二个参数，该方法会分析base_url的scheme、netloc和
path这3个内容并对新链接缺失的部分进行补充，最后返回结果。

base_url提供了三项内容scheme、netloc和path。如果这3项在新的链接里不存在，就予以补充；
如果新的链接存在，就使用新的链接的部分。

base_url中的params、query和fragment是不起作用的。
'''
'''
from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))
'''

'''
6. urlencode()

在构造GET请求参数的时候非常有用,首先声明了一个字典来将参数表示出来，然后调用urlencode()方法将其序列化为GET请求参数。
'''
'''
from urllib.parse import urlencode

params = {
    'country':'china',
    'name':'germey',
    'age':23
} 

base_url = 'http://www.baidu.com?'

url = base_url + urlencode(params)

print(url)
'''

'''
7. parse_qs()

反序列化。如果我们有一串GET请求参数，利用parse_qs()方法，就可以将它转回字典。
'''
'''
from urllib.parse import parse_qs
 
query = 'name=germey&age=22'
print(parse_qs(query))
'''

'''
8. parse_qsl()

用于将参数转化为元组组成的列表。
'''
'''
from urllib.parse import parse_qsl
 
query = 'name=germey&age=22'
print(parse_qsl(query))
'''

'''
9. quote()

该方法可将内容转化为URL编码格式，URL中带有中文参数时，有时可能会导致乱码的问题，此时用
这个方法可以将中文字符转化为URL编码。
'''
'''
from urllib.parse import quote

keyword = '汽车'

url = 'https://www.baidu.com/s?wd=' + quote(keyword)

print(url)
'''

'''
10. unquote()

可以进行URL解码。
'''
'''
from urllib.parse import unquote
 
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
'''
