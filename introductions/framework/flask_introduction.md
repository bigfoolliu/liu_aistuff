# flask框架介绍以及flask源码阅读体会

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1特点](#1.1特点)

<!-- vim-markdown-toc -->

## 1.概述

### 1.1特点

- [flask官方中文文档](https://dormousehole.readthedocs.io/en/latest/)


1. 轻量级web框架，只有一个内核，默认依赖两个外部库：Jinja2 模板引擎和 Werkzeug WSGI 工具集，自由，灵活，可扩展性强，开发者可以根据需求自己造轮子
2. 适用于做小型网站以及web服务的API，开发大型网站无压力，但架构需自行设计
3. 与sql结合不弱于Django，而与nosql的结合远远优于Django
4. 开发成本取决于开发者的能力和经验
5. 各方面性能均等于或优于Django

