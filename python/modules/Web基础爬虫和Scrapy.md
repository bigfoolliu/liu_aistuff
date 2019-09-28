# Web基础, 爬虫和Scrapy

## 1. 简单介绍

&ensp;&ensp;&ensp;&ensp;Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。

&ensp;&ensp;&ensp;&ensp;其最初是为了网络抓取所设计的， 也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。

 </br>

## 2. 其他强大特性

&ensp;&ensp;&ensp;&ensp;Scrapy提供了很多强大的特性来使得爬取更为简单高效, 例如:

1. 对HTML, XML源数据 选择及提取 的内置支持, 提供了CSS选择器(selector)以及XPath表达式进行处理， 以及一些帮助函数(helper method)来使用正则表达式来提取数据。

2. 提供 交互式shell终端 , 为您测试CSS及XPath表达式，编写和调试爬虫提供了极大的方便。

3. 通过 feed导出 提供了多格式(JSON、CSV、XML)，多存储后端(FTP、S3、本地文件系统)的内置支持。

4. 提供了一系列在spider之间共享的可复用的过滤器(即 Item Loaders)，对智能处理爬取数据提供了内置支持。

5. 针对非英语语系中不标准或者错误的编码声明, 提供了自动检测以及健壮的编码支持。

6. 高扩展性。您可以通过使用 signals ，设计好的API(中间件, extensions, pipelines)来定制实现您的功能。

7. 内置的中间件及扩展为下列功能提供了支持: \*cookies and session 处理 \*HTTP 压缩 \*HTTP 认证 \*HTTP 缓存 \*user-agent模拟 \*robots.txt \*爬取深度限制 \*其他。

8. 内置 Telnet终端 ，通过在Scrapy进程中钩入Python终端，使您可以查看并且调试爬虫。

9. 以及其他一些特性，例如可重用的，从 Sitemaps 及 XML/CSV feeds中爬取网站的爬虫、 可以 自动下载 爬取到的数据中的图片(或者其他资源)的media pipeline、 带缓存的DNS解析器，以及更多的特性。

 </br>

## 3. 架构

Scrapy的架构图如下：
</br>
![scrapy架构图](res/scrapy_architecture.png "scrapy架构图")
</br>

 </br>

## 4. HTTP基本原理

### 4.1 URI和URL

&ensp;&ensp;&ensp;&ensp;URI的全称为Uniform Resource Identifier，即统一资源标志符，URL的全称为Universal Resource Locator，即统一资源定位符。

&ensp;&ensp;&ensp;&ensp;URI还包括一个子类叫作URN，它的全称为Universal Resource Name，即统一资源名称。

### 4.2 超文本

&ensp;&ensp;&ensp;&ensp;英文名称叫作hypertext，网页的源代码HTML就可以称作超文本，由浏览器解析而成。

### 4.3 HTTP和HTTPS

&ensp;&ensp;&ensp;&ensp;URL的开头会有http或https，这就是访问资源需要的协议类型。有时，我们还会看到ftp、sftp、smb、file开头的URL，它们都是协议类型。

&ensp;&ensp;&ensp;&ensp;HTTP的全称是Hyper Text Transfer Protocol，中文名叫作超文本传输协议。

&ensp;&ensp;&ensp;&ensp;HTTPS的全称是Hyper Text Transfer Protocol over Secure Socket Layer，是以安全为目标的HTTP通道，简单讲是HTTP的安全版，即HTTP下加入SSL层，简称为HTTPS。HTTPS的安全基础是SSL，因此通过它传输的内容都是经过SSL加密。

### 4.4 HTTP请求过程

&ensp;&ensp;&ensp;&ensp;客户端向服务器发送Requests(请求)；服务器收到请求，向客户端发送Response(响应)。此处客户端即代表我们自己的PC或手机浏览器，服务器即要访问的网站所在的服务器。</br>
网站请求Network面板内容解释：</br>
|名称|含义|
|---|---|
|第一列Name|请求的名称，一般会将URL的最后一部分内容当作名称|
|第二列Status|响应的状态码，这里显示为200，代表响应是正常的。通过状态码，我们可以判断发送了请求之后是否得到了正常的响应|
|第三列Type|请求的文档类型。为document，代表我们这次请求的是一个HTML文档，内容就是一些HTML代码|
|第四列Initiator|请求源。用来标记请求是由哪个对象或进程发起的|
|第五列Size|从服务器下载的文件和请求的资源大小。如果是从缓存中取得的资源，则该列会显示from cache|
|第六列Time|发起请求到获取响应所用的总时间|
|第七列Waterfall|网络请求的可视化瀑布流|

### 4.5 请求

#### 4.5.1 请求方法

常见的请求方法有两种：GET和POST。

在浏览器中直接输入URL并回车，这便发起了一个GET请求。</br>
POST请求大多在表单提交时发起。比如，对于一个登录表单，输入用户名和密码后，点击“登录”按钮，这通常会发起一个POST请求，其数据通常以表单的形式传输，而不会体现在URL中。

#### 4.5.2 请求网址

即URL。

#### 4.5.3 请求头

Accept：请求报头域，用于指定客户端可接受哪些类型的信息。</br>
Accept-Language：指定客户端可接受的语言类型。</br>
Accept-Encoding：指定客户端可接受的内容编码。</br>
Host：用于指定请求资源的主机IP和端口号，其内容为请求URL的原始服务器或网关的位置。</br>
Cookie(s)：网站为了辨别用户进行会话跟踪而存储在本地的数据。主要功能是维持当前访问数据。</br>
Regerer：此内容用来标识这个请求是从哪个页面发过来的，服务器可以拿到这一信息并做相应的处理，如作来源统计、防盗链处理等。</br>
User-Agent：特殊的字符串头，可以使服务器识别客户使用的操作系统及版本，浏览器及版本等信息。</br>
Content-Type：用来表示具体请求中的媒体类型信息。</br>

#### 4.5.4 请求体

请求体承载的内容是POST请求中的表单数据，而对于GET请求，请求体则为空。

#### 4.5.5 响应

响应，由服务端返回给客户端，可以分为三部分：响应状态码（Response Status Code）、响应头（Response Headers）和响应体（Response Body）。

##### 4.5.5.1 响应状态码

表示服务器响应状态，200表示服务器响应正常，400表示页面未找到，500代表服务器内发生错误。其他错误代码及错误原因如下表：</br>
|状态码   |说明   |详情|
|:---:|:---|:---|
|100   |继续   |请求者应当继续提出请求。服务器已收到请求的一部分，正在等待其余部分   |
|101   |切换协议   |请求者已要求服务器切换协议，服务器已确认并准备切换   |
|200   |成功   |服务器已成功处理了请求   |
|201   |已创建   |请求成功并且服务器创建了新的资源   |
|202   |已接受   |服务器已接受请求，但尚未处理   |
|203   |非授权信息   |服务器已成功处理了请求，但返回的信息可能来自另一个源   |
|204   |无内容   |服务器成功处理了请求，但没有返回任何内容   |
|205   |重置内容   |服务器成功处理了请求，内容被重置   |
|206   |部分内容   |服务器成功处理了部分请求   |
|300   |多种选择   |针对请求，服务器可执行多种操作   |
|301   |永久移动   |请求的网页已永久移动到新位置，即永久重定向   |
|302   |临时移动   |请求的网页暂时跳转到其他页面，即暂时重定向   |
|303   |查看其他位置   |如果原来的请求是POST，重定向目标文档应该通过GET提取   |
|304   |未修改   |此次请求返回的网页未修改，继续使用上次的资源   |
|305   |使用代理   |请求者应该使用代理访问该网页   |
|307   |临时重定向   |请求的资源临时从其他位置响应   |
|400   |错误请求   |服务器无法解析该请求   |
|401   |未授权   |请求没有进行身份验证或验证未通过   |
|403   |禁止访问   |服务器拒绝此请求   |
|404   |未找到   |服务器找不到请求的网页   |
|405   |方法禁用   |服务器禁用了请求中指定的方法   |
|406   |不接受   |无法使用请求的内容响应请求的网页   |
|407   |需要代理授权   |请求者需要使用代理授权   |
|408   |请求超时   |服务器请求超时   |
|409   |冲突   |服务器在完成请求时发生冲突   |
|410   |已删除   |请求的资源已永久删除   |
|411   |需要有效长度   |服务器不接受不含有效内容长度标头字段的请求   |
|412   |未满足前提条件   |服务器未满足请求者在请求中设置的其中一个前提条件   |
|413   |请求实体过大   |请求实体过大，超出服务器的处理能力   |
|414   |请求URI过长   |请求网址过长，服务器无法处理   |
|415   |不支持类型   |请求格式不被请求页面支持   |
|416   |请求范围不符   |页面无法提供请求的范围   |
|417   |未满足期望值   |服务器未满足期望请求标头字段的要求   |
|500   |服务器内部错误   |服务器遇到错误，无法完成请求   |
|501   |未实现   |服务器不具备完成请求的功能   |
|502   |错误网关   |服务器作为网关或代理，从上游服务器收到无效响应   |
|503   |服务不可用   |服务器目前无法使用   |
|504   |网关超时   |服务器作为网关或代理，但是没有及时从上游服务器收到请求   |
|505   |HTTP版本不支持   |服务器不支持请求中所用的HTTP协议版本   |
|

##### 4.5.5.2 响应头

包含了服务器对请求的应答信息。

1. Date：标识响应产生的时间。</br>
2. Last-Modified：指定资源的最后修改时间。</br>
3. Content-Ending：指定响应内容的编码。</br>
4. Content-Type：文档类型，指定返回的数据类型是什么，如text/html代表返回HTML文档，application/x-javascript则代表返回JavaScript文件，image/jpeg则代表返回图片。</br>
5. Set-Cookie：设置Cookies。</br>
6. Expires：指定响应的过期时间，可以使代理服务器或浏览器将加载的内容更新到缓存中。</br>

##### 4.5.5.3 响应体

&ensp;&ensp;&ensp;&ensp;响应的正文数据都在响应体中，比如请求网页时，它的响应体就是网页的HTML代码；请求一张图片时，它的响应体就是图片的二进制数据。我们做爬虫请求网页后，要解析的内容就是响应体。

在做爬虫时，我们主要通过响应体得到网页的源代码、JSON数据等，然后从中做相应内容的提取。

 </br>

## 5. 网页基础

### 5.1 网页的组成

三大部分组成：HTML，JavaScript，Css。

#### 5.1.1 HTML

全称叫作Hyper Text Markup Language，即超文本标记语言。</br>
包括文字(img标签)，视频(video标签)，段落(p标签)，按钮(button标签)等元素。元素之间的布局通过布局标签div嵌套组合而成。</br>

#### 5.1.2 CSS

全称叫作Cascading Style Sheets，即层叠样式表。</br>
层叠”是指当在HTML中引用了数个样式文件，并且样式发生冲突时，浏览器能依据层叠顺序处理。“样式”指网页中文字大小、颜色、元素间距、排列等格式。</br>

在网页中，一般会统一定义整个网页的样式规则，并写入CSS文件中（其后缀为css）。在HTML中，只需要用link标签即可引入写好的CSS文件，这样整个页面就会变得美观、优雅。

#### 5.1.3 JavaScript

配合HTML和CSS，使页面产生交互效果。在HTML页面中以script标签引入。

### 5.2 网页的结构

可参照实例：[html_demo](file:///C:/Users/tonyl/Documents/GitHub/module_learning/html_demo.html)

这个实例便是网页的一般结构。一个网页的标准形式是html标签内嵌套head和body标签，head内定义网页的配置和引用，body内定义网页的正文。

### 5.3 节点树及节点间的关系

在HTML中，所有标签定义的内容都是节点，它们构成了一个HTML DOM树。

DOM全称为Document Object Model，即文档对象模型，其定义了访问HTML和XML的标准。具体可参照[HTML DOM节点](http://www.w3school.com.cn/htmldom/dom_nodes.asp)

### 5.4 选择器

通过CSS选择器，网页上不同的节点会根据不同的节点设置不同的样式规则。常用的选择器是XPath。

 </br>

## 6. 爬虫的基本原理

### 6.1 爬虫概述

爬虫即获取网页并提取和保存信息的自动化程序。

#### 6.1.1 获取网页

&ensp;&ensp;&ensp;&ensp;通过urllib、requests等库，我们可以实现HTTP请求操作，请求和响应都可以用类库提供的数据结构来表示，得到响应之后只需要解析数据结构中的Body部分即可，即得到网页的源代码，这样我们可以用程序来实现获取网页。

#### 6.1.2 提取信息

&ensp;&ensp;&ensp;&ensp;最通用的方法便是采用正则表达式提取，这是一个万能的方法，但是在构造正则表达式时比较复杂且容易出错。</br>
&ensp;&ensp;&ensp;&ensp;另外，由于网页的结构有一定的规则，所以还有一些根据网页节点属性、CSS选择器或XPath来提取网页信息的库，如Beautiful Soup、pyquery、lxml等。使用这些库，我们可以高效快速地从中提取网页信息，如节点的属性、文本值等。

#### 6.1.3 保存数据

&ensp;&ensp;&ensp;&ensp;保存形式有多种多样，如可以简单保存为TXT文本或JSON文本，也可以保存到数据库，如MySQL和MongoDB等，也可保存至远程服务器，如借助SFTP进行操作等。

### 6.2 可抓取数据类型

1. HTML源代码

2. JSON字符串

3. 二进制数据(如图片，视频，音频等)

4. CSS，JavaScript和配置文件等基于HTTP或HTTPS协议的数据

### 6.3 JavaScript渲染页面

&ensp;&ensp;&ensp;&ensp;现在网页越来越多地采用Ajax、前端模块化工具来构建，整个网页可能都是由JavaScript渲染出来的，也就是说原始的HTML代码就是一个空壳。

&ensp;&ensp;&ensp;&ensp;使用基本HTTP请求库得到的源代码可能跟浏览器中的页面源代码不太一样。对于这样的情况，我们可以分析其后台Ajax接口，也可使用Selenium、Splash这样的库来实现模拟JavaScript渲染。

## 7. 会话及cookie

### 7.1 静态网页及动态网页

这种网页的内容是HTML代码编写的，文字、图片等内容均通过写好的HTML代码来指定，这种页面叫作静态网页。它加载速度快，编写简单，但是存在很大的缺陷，如可维护性差，不能根据URL灵活多变地显示内容等。例如，我们想要给这个网页的URL传入一个name参数，让其在网页中显示出来，是无法做到的。

动态网页可以动态解析URL中参数的变化，关联数据库并动态呈现不同的页面内容，非常灵活多变。我们现在遇到的大多数网站都是动态网站，它们不再是一个简单的HTML，而是可能由JSP、PHP、Python等语言编写的，并且其可实现用户登录和注册的功能。

### 7.2 无状态HTTP

指HTTP协议对事务处理无记忆能力，即服务器不知道客户端是什么状态。后续处理信息就需要重新传递前面的请求，因此浪费资源。

会话和Cookies解决这个问题，可以用于保持HTTP连接状态。下次请求时携带Cookies发送请求，不必重新输入用户名，密码等信息。

#### 7.2.1 会话

来的含义是指有始有终的一系列动作/消息。</br>
在Web中，会话对象用来存储特定用户会话所需的属性及配置信息。让程序在Web页跳转时，存储在会话对象中的变量不会丢失。

#### 7.2.2 Cookies

Cookies指某些网站为了辨别用户身份、进行会话跟踪而存储在用户本地终端上的数据。

#### 7.2.3 会话维持

利用Cookies保持状态：

1. 客户端第一次请求服务器；

2. 服务器返回一个请求头中带'Set-Cookie'字段的响应给客户端，用来标记是哪一个用户；

3. 客户端保存Cookies；

4. 浏览器再次请求该网站，浏览器将Cookies放到请求头一起提交给服务器；

5. 服务器检测到Cookies中携带的会话ID信息，即可找到对应的会话，判断会话来辨认用户的状态；

&ensp;&ensp;&ensp;&ensp;在成功登录某个网站时，服务器会告诉客户端设置哪些Cookies信息，在后续访问页面时客户端会把Cookies发送给服务器，服务器再找到对应的会话加以判断。如果会话中的某些设置登录状态的变量是有效的，那就证明用户处于登录状态，此时返回登录之后才可以查看的网页内容，浏览器再进行解析便可以看到了。反之，如果传给服务器的Cookies是无效的，或者会话已经过期了，我们将不能继续访问页面，此时可能会收到错误的响应或者跳转到登录页面重新登录。所以，Cookies和会话需要配合，一个处于客户端，一个处于服务端，二者共同协作，就实现了登录会话控制。

程序一般都是在我们做注销操作时才去删除会话。不是关闭浏览器，会话就消失，只有程序通知服务器删除一个会话，否则服务器会一直保留。

## 8. 代理

实现IP伪装，让服务器识别不出是由我们本机发起的请求，防止'封IP'。

### 8.1 代理的基本原理

代理指代理服务器，proxy server。功能是代理网络用户去获得网络信息</br>
本机将请求发给代理服务器，代理服务器将请求发给Web服务器，Web服务器将响应返回给代理服务器，代理服务器将响应返回给本机，这个过程就实现了IP伪装。

### 8.2 代理的作用

1. 突破自身IP访问限制，访问平时不能访问的站点。

2. 访问一些单位或团体内部资源：比如使用教育网内地址段免费代理服务器，就可以用于对教育网开放的各类FTP下载上传，以及各类资料查询共享等服务。

3. 提高访问速度：访问一些单位或团体内部资源：比如使用教育网内地址段免费代理服务器，就可以用于对教育网开放的各类FTP下载上传，以及各类资料查询共享等服务。

4. 隐藏真实IP：上网者也可以通过这种方法隐藏自己的IP，免受攻击。对于爬虫来说，我们用代理就是为了隐藏自身IP，防止自身的IP被封锁。

### 8.3 代理的分类

根据协议区分：</br>
|类别   |作用   |
|---|---|
|FTP代理服务器   |主要用于访问FTP服务器，一般有上传、下载以及缓存功能，端口一般为21、2121等   |
|HTTP代理服务器|主要用于访问网页，一般有内容过滤和缓存功能，端口一般为80、8080、3128等|
|SSL/TLS代理服务    |主要用于访问加密网站，一般有SSL或TLS加密功能（最高支持128位加密强度），端口一般为443   |
|RTSP代理    |主要用于访问Real流媒体服务器，一般有缓存功能，端口一般为554   |
|Telnet代理    |主要用于telnet远程控制（黑客入侵计算机时常用于隐藏身份），端口一般为23   |
|POP3/SMTP代理    |主要用于POP3/SMTP方式收发邮件，一般有缓存功能，端口一般为110/25   |
|SOCKS代理    |只是单纯传递数据包，不关心具体协议和用法，所以速度快很多，一般有缓存功能，端口一般为1080。SOCKS代理协议又分为SOCKS4和SOCKS5，前者只支持TCP，而后者支持TCP和UDP，还支持各种身份验证机制、服务器端域名解析等。简单来说，SOCK4能做到的SOCKS5都可以做到，但SOCKS5能做到的SOCK4不一定能做到。   |
|

根据匿名程度区分：</br>
|类别   |详情   |
|---|---|
|高度匿名代理   |数据包原封不动的转发，服务端看来就是普通用户，而记录的IP为代理的IP   |
|普通匿名代理   |数据包有所改动，服务端有可能发现为代理并追查到客户端IP，代理服务器通常会加入的HTTP头为HTTP_VIA和HTTP_X_FORWARD_FOR   |
|透明代理   |数据包改动且告诉服务器客户端的真实IP，主要用缓存技术提高浏览速度，用内容过滤提高安全性，常见例子是内网中的硬件防火墙   |
|间谍代理   |组织或个人创建的用于记录用户传输的数据，然后进行研究、监控等目的的代理服务器   |
|

### 8.4 常见代理设置

1. 网上的免费代理，可用的不多

2. 使用付费代理服务

3. ADSL拨号，拨一次号换一次IP，稳定性高

## 9. 基本库的使用

pyhton基础的HTTP库有：urlib，requests，httplib2，trep。

### 9.1 urlib库

内置的库，包含四个模块：

1. request：模拟发送请求，代码实例：[request_module](C:/Users/tonyl/Documents/GitHub/module_learning/request_module.py)。

2. error：异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止。代码实例：[error_module](C:/Users/tonyl/Documents/GitHub/module_learning/error_module.py)

3. parse：一个工具模块，提供了许多URL处理方法，比如拆分、解析、合并等。代码实例：[parse_module](C:/Users/tonyl/Documents/GitHub/module_learning/parse_module.py)

4. robotparser：主要是用来识别网站的robots.txt文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。代码实例：[robotparser_module](C:/Users/tonyl/Documents/GitHub/module_learning/robotparser_module.py)

### 9.2 requests库

在处理Cookies，登录验证，代理设置操作更加方便。

代码实例：[requests_module](C:/Users/tonyl/Documents/GitHub/module_learning/requests_module.py)

### 9.3 正则表达式(Regular Expression),RE

可以用来匹配处理字符串，通常用来检索，替换那些符合某个模式(规则)的文本。

由于正则表达式主要应用对象是文本，因此它在各种文本编辑器场合都有应用，小到著名编辑器EditPlus，大到Microsoft Word、Visual Studio等大型编辑器，都可以使用正则表达式来处理文本内容。

正则表达式测试工具：[正则表达式测试工具](http://tool.oschina.net/regex)

正则表达式代码实例：[re_module](C:/Users/tonyl/Documents/GitHub/module_learning/re_module.py)

常用的正则表达式匹配规则如下:</br>
|模式   |描述   |
|:---:|:---|
|.   |表示匹配除了换行符之外的任意字符   |
|^   |（脱字符）匹配输入字符串的起始位置   |
|$   |（美元符号）匹配输入字符串的结束位置   |
|\|   |a\|b，表示匹配a或b   |
|\   |将普通字符转为特殊字符，如\d表示任意十进制数字，\\.表示匹配点号本身  |
|*   |匹配前面的子表达式零次或多次，等价于{0,}   |
|+   |匹配前面的子表达式一次或多次，等价于{1,}   |
|?   |匹配前面的子表达式零次或一次，等价于{0,1}   |
|{m,n}   |m<=n，且均为非负整数，表示前面的RE表达式匹配m~n次，{m}表示匹配m次，{m,}表示至少匹配m次，{,n}表示需要匹配最多匹配n次   |
|()   |匹配括号内的表达式，也表示一个组   |
|[ ]   |匹配括号内包含的任意一个字符，出现连字符-在中间则表示字符范围描述，首位出现^表示不匹配不包含其中的任意字符   |
|\n   |匹配一个换行符   |
|\t   |匹配一个制表符   |
|\d   |匹配任意十进制数字，等价于[0-9]   |
|\D   |匹配任意非数字的字符   |
|\w   |匹配字母，数字，下划线   |
|\W   |匹配不是字母，数字，下划线的字符  |
|\s   |匹配任意空白字符，等价于[\t\n\r\f]   |
|\S   |匹配任意非空字符   |
|\z   |匹配字符串结尾，如果存在换行，同时还会匹配换行符   |
|\Z   |匹配字符串结尾，如果存在换行，只匹配换行符前的结束字符串   |
|\A   |匹配字符串开头   |
|   |   |

常用修饰符:</br>
|修饰符   |描述   |
|:---:|:---|
|re.S（常用）   |使.匹配包括换行在内的所有字符   |
|re.X（常用）   |该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解   |
|re.I   |使匹配对大小写不敏感   |
|re.L   |做本地化识别（locale-aware）匹配   |
|re.M   |多行匹配，影响^和$   |
|re.U   |根据Unicode字符集解析字符。这个标志影响\w、\W、 \b和\B   |
|   |   |

### 9.4 猫眼Top100电影信息抓取

参考代码：[maoyan_top100](C:/Users/tonyl/Documents/GitHub/module_learning/maoyan_top100.py)

## 10. 解析数据之解析库的使用

### 10.1 使用XPath

全称为XML Path Language，用于在XML文档中查找信息的语言，也可用于HTML文档搜索。</br>
更多XPath用法参照：[XPath](http://www.w3school.com.cn/xpath/index.asp)</br>
更多Python lxml库的用法：[Python lxml](http://lxml.de/)

常用的几个规则如下：</br>
|表达式   |描述   |
|:---:|:---|
|nodename   |选取此节点的所有子节点   |
|/   |从当前节点选取直接子节点   |
|//   |从当前节点选取子孙节点   |
|.   |选取当前节点   |
|..   |选取当前节点的父节点   |
|@   |选取属性   |
|   |   |

常用匹配规则：//title[@lang='eng']，它代表选择所有名称为title，同时属性lang的值为eng的节点

参考代码：[lxml_module](C:/Users/tonyl/Documents/GitHub/module_learning/lxml_module.py)

### 10.2 使用Beautiful Soup

Beautiful Soup提供一些简单的、Python式的函数来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。</br>
Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为UTF-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时你仅仅需要说明一下原始编码方式就可以了。</br>
Beautiful Soup已成为和lxml、html6lib一样出色的Python解释器，为用户灵活地提供不同的解析策略或强劲的速度。

解析时依赖于解析器：</br>
|解析器   |使用方法   |优点  |
|:---:|:---|:---|
|python标准库   |BeautifulSoup(markup, 'html.parser')   |Python的内置标准库、执行速度适中、文档容错能力强|
|lxml HTML解析器    |BeautifulSoup(markup, 'lxml')    |速度快、文档容错能力强    |
|lxml XML解析器    |BeautifulSoup(markup, 'xml')    |速度快、唯一支持XML的解析器   |
|html5lib    |BeautifulSoup(markup, 'html5lib')    |最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档    |
|    |    |    |

参考代码：[beautifulsoup_module](C:/Users/tonyl/Documents/GitHub/module_learning/beautifulsoup_module.py)

### 10.3 使用pyquery

如果你对Web有所涉及，如果你比较喜欢用CSS选择器，如果你对jQuery有所了解，那么这里有一个更适合你的解析库——pyquery。</br>
可参考网址：[pyquery](https://cuiqingcai.com/5551.html)</br>
参考代码：[pyquery_module](C:/Users/tonyl/Documents/GitHub/module_learning/pyquery_module.py)

## 11. 数据存储

解析出数据之后就是存储数据，保存的形式可以为TXT，JSON，CSV等，还可以保存到关系型数据库MySQL，非关系型数据库MongoDB，Redis等。

### 11.1 TXT文本存储

操作简单，几乎兼容任何平台，但不利于检索。

参考代码：[txt_saving](C:/Users/tonyl/Documents/GitHub/module_learning/txt_saving.py)

### 11.2 JSON文件存储

全称JavaScript Object Notation，即JavaScript对象标记，它通过对象和数组的组合来表示数据，构造简洁但是结构化程度非常高，是一种轻量级的数据交换格式。

#### 11.2.1 对象和数组

JavaScript语言中，一切均为对象。字符串，数组，对象，数字均可由JSON表示。可以无限次嵌套。</br>
对象：{key1:value1, key2:value2, ...}</br>
数组：["c", "java", "python", ...]

#### 11.2.2 读取JSON

参考代码：[json_saving](C:/Users/tonyl/Documents/GitHub/module_learning/json_saving.py)

### 11.3 CSV文件存储

CSV，全称Comma-Separated Values，即逗号分隔符或字符分隔符，其文件以纯文本形式存储表格数据。

参考代码：[csv_saving](C:/Users/tonyl/Documents/GitHub/module_learning/csv_saving.py)

## 11.4 关系型数据库存储

&ensp;&ensp;&ensp;&ensp;关系型数据库是基于关系模型的数据库，而关系模型是通过二维表来保存的，所以它的存储方式就是行列组成的表，每一列是一个字段，每一行是一条记录。表可以看作某个实体的集合，而实体之间存在联系，这就需要表与表之间的关联关系来体现，如主键外键的关联关系。多个表组成一个数据库，也就是关系型数据库。</br>
&ensp;&ensp;&ensp;&ensp;关系型数据库有多种，如SQLite、MySQL、Oracle、SQL Server、DB2等。

### 11.4.1 MySQL存储

在WEB应用方面MySQL是最好的RDBMS(Relational Database Management System：关系数据库管理系统)应用软件之一。</br>
教程参照：[菜鸟教程-MySQL](http://www.runoob.com/mysql/mysql-tutorial.html)

参考代码：[mysql_saving](C:/Users/tonyl/Documents/GitHub/module_learning/mysql_saving.py)

## 11.5 非关系型数据存储

非关系型数据库又可细分如下。

键值存储数据库：代表有Redis、Voldemort和Oracle BDB等。
列存储数据库：代表有Cassandra、HBase和Riak等。
文档型数据库：代表有CouchDB和MongoDB等。
图形数据库：代表有Neo4J、InfoGrid和Infinite Graph等。

对于爬虫的数据存储来说，一条数据可能存在某些字段提取失败而缺失的情况，而且数据可能随时调整。另外，数据之间还存在嵌套关系。如果使用关系型数据库存储，一是需要提前建表，二是如果存在数据嵌套关系的话，需要进行序列化操作才可以存储，这非常不方便。如果用了非关系型数据库，就可以避免一些麻烦，更简单高效。

### 11.5.1 MongoDB存储

C++编写的基于分布式文件存储的开源数据库系统。内容存储形式类似JSON对象。</br>
字段值可以包含其他文档，数组，文档数组。

参考网址：[MongoDB存储](https://cuiqingcai.com/5584.html)

### 11.5.2 Redis存储

Redis是一个基于内存的高效的键值型非关系型数据库，存取效率极高，而且支持多种存储数据结构，使用也非常简单。

参考网址：[Redis存储](https://cuiqingcai.com/5587.html)

## 12. Ajax数据爬取

即“Asynchronous Javascript And XML”（异步 JavaScript 和 XML），是指一种创建交互式网页应用的网页开发技术。Ajax 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

参考代码：[ajax_dataminning](C:/Users/tonyl/Documents/GitHub/module_learning/ajax_dataminning.py)

## 13. 动态渲染页面爬取

JavaScript动态渲染页面方式除了Ajax还有其他方式，分页部分是由JavaScript生成，不是原始HTML代码，不包含Ajax请求。</br>
因此，直接使用模拟浏览器运行的方式来实现，就可以做到在浏览器中看到的是什么样，抓取的源码就是什么样，即可见即可爬。不需要考虑网页内部的JavaScript用了什么算法渲染页面，不必考虑网页后台Ajax接口有哪些参数。</br>
python常见模拟浏览器运行的库有：Selemium，Splash，PyV8，Ghost等。

### 13.1 Selenium使用

selenium是一个自动化测试工具，可以驱动浏览器执行特定的动作，如点击，下拉等操作，还可以获取浏览器当前呈现的页面的源代码，做到所见即所爬。

通常配合chrome浏览器（需配置chromedriver）使用。

参考代码：[selenium_module](C:/Users/tonyl/Documents/GitHub/module_learning/selenium_module.py)

### 13.2 Splash使用

Splash是一个JavaScript渲染服务，是一个带有Http API的轻量级浏览器。与Selenium功能类似，可对接Twisted库和QT库，实现动态渲染页面的抓取。</br>
功能还包括：

1. 异步方式处理多个网页渲染过程

2. 获取渲染后的网页的源码或截图

3. 通过关闭图片渲染或者使用Adblock加快页面渲染

4. 可执行特定的JS脚本

5. 可通过Lua脚本控制页面渲染过程

6. 获取渲染的详细过程并通过HAR（HTTP Archive）格式呈现

可参考：[Splash使用](https://cuiqingcai.com/5638.html)
