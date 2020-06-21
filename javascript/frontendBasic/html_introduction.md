# html介绍

<!-- TOC -->

- [html介绍](#html%e4%bb%8b%e7%bb%8d)
  - [1.html基础](#1html%e5%9f%ba%e7%a1%80)
  - [2.html标签](#2html%e6%a0%87%e7%ad%be)
    - [2.1html标签种类](#21html%e6%a0%87%e7%ad%be%e7%a7%8d%e7%b1%bb)
    - [2.2html标签属性](#22html%e6%a0%87%e7%ad%be%e5%b1%9e%e6%80%a7)
      - [2.2.1通用标签属性](#221%e9%80%9a%e7%94%a8%e6%a0%87%e7%ad%be%e5%b1%9e%e6%80%a7)
      - [2.2.2非通用标签属性](#222%e9%9d%9e%e9%80%9a%e7%94%a8%e6%a0%87%e7%ad%be%e5%b1%9e%e6%80%a7)
  - [3.html样式](#3html%e6%a0%b7%e5%bc%8f)
    - [3.1样式引入方式](#31%e6%a0%b7%e5%bc%8f%e5%bc%95%e5%85%a5%e6%96%b9%e5%bc%8f)
  - [4.html实体](#4html%e5%ae%9e%e4%bd%93)
  - [5.XHTML使用](#5xhtml%e4%bd%bf%e7%94%a8)
  - [6.网页编排原则](#6%e7%bd%91%e9%a1%b5%e7%bc%96%e6%8e%92%e5%8e%9f%e5%88%99)

<!-- /TOC -->

## 1.html基础

- [w3c school的html教程](https://www.w3school.com.cn/html/index.asp)

## 2.html标签

### 2.1html标签种类

- [html标签参考](https://www.w3school.com.cn/tags/index.asp)

| 标签 | 含义 |
| :---: | :--- |
| `<!DOCTYPE html>` | 声明html的版本，此为html5的申明 |
| `<head></head>` | 声明一些编码格式，标题，文字显示形式（中英文） |
| style | 样式定义 |
| link | 资源引用 |
| p | 段落 |
| a | 超链接 |
| img | 图片 |
| table | 定义表格 |
| caption | 定义表格标题 |
| th | 定义表格表头 |
| tr | 定义表格行 |
| td | 定义表格单元 |
| thead | 定义表格页眉 |
| tbody | 定义表格主体 |
| tfoot | 定义表格页脚 |
| col | 定义表格列属性 |
| ul | 无序列表 |
| ol | 有序列表 |
| li | 列表项(无序) |
| dl | 自定义列表 |
| dt | 自定义列表项 |
| dd | 自定义描述 |
| div | 块 |
| form | 表单 |
| input | 输入按钮，单选框等 |
| select | 下拉框 |
| option | 下拉框选项 |
| textarea | 文本域 |
| frame | 框架 |
| frameset | 框架集 |
| iframe | 内联框架 |
| article | 代表文档，页面或者其他被外部应用的内容，可嵌套，可用来表示插件 |
| section | 对网站或者页面上的内容进行分块 |
| nav | 导航元素，导航条，侧边栏导航，页面导航，翻页操作 |
| aside | 表示当前页面附属信息，侧边栏，广告，导航条等 |
| time | 时间表示，该元素能够以机器可读的方式对时间进行编码 |
| footer | 底部栏信息 |
| header | 头部栏信息 |
| address | 呈现联系信息 |
| label | 为input元素定义标注 |
|  |  |

### 2.2html标签属性

#### 2.2.1通用标签属性

| 属性 | 含义 |
| :---: | :--- |
| class | 规定元素的类名 |
| id | 规定元素的唯一id |
| style | 规定元素的样式 |
| title | 规定元素的额外信息 |
| float |  |
|  |  |

#### 2.2.2非通用标签属性

**h标签属性：**

| 属性 | 含义 |
| :---: | :--- |
| align | 对齐方式，有`center` `left` `right`等 |
|  |  |
|  |  |

**body标签属性：**

| 属性 | 含义 |
| :---: | :--- |
| bgcolor | 背景颜色，有`#FFFFFF` `red`等，红绿蓝各自由两个16进制数字表示 |
| background | 背景，可以为图片 |
|  |  |

**a标签属性：**

| 属性 | 含义 |
| :---: | :--- |
| href | 规定链接指向页面的url |
| target | 规定在何处打开超链接，`_blank`表示在新页面打开，不覆盖原来页面；`_self`是默认的，覆盖原有标签 |
| name | 创建文档内的链接 |
|  |  |

**link标签属性：**

| 属性 | 含义 |
| :---: | :--- |
| rel | 表示样式类型，`stylesheet`表示外部样式表 |
| type | 表示文档引入的类型，`text/css`表示引入的文档类型为css文件 |
| href | 表示引入文档的位置 |
|  |  |

**img标签属性：**

| 属性 | 含义 |
| :---: | :--- |
| alt | 指定图片名字，即使图片没有显示 |
| width | 宽度 |
|  |  |

## 3.html样式

### 3.1样式引入方式

1. 外部样式表

    ```html
    <head>
        <link rel="stylesheet" type="text/css" href="mystyle.css">
    </head>
    ```

2. 内部样式表

    ```html
    <head>
        <style type="text/css">
            div {
                width: 100px;
                height: 100px;
            }
        </style>
    </head>
    ```

3. 内联样式表

    ```html
    <body>
        <div style="width:100px; height:100px; background:red">
    </body>
    ```

## 4.html实体

- html中预留字符串必须被替换为字符实体，即`转义`
- [html实体参考手册](https://www.w3cschool.cn/htmltags/html-symbols.html)
- [html实体参考手册（常用版）](https://www.w3school.com.cn/html/html_entities.asp)

| 字符 | html中的字符 |
| :---: | :--- |
| < | `&lt;` |
| > | `&gt;` |
| & | `&amp;` |
| " | `&quot;` |
|  |  |

## 5.XHTML使用

- 可扩展的html，与html4.01几乎相同，更严格
- 以xml应用的方式定义的html
- 可以使html的代码更加规范，易读

## 6.网页编排原则
