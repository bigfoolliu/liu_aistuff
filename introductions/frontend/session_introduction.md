# session

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)

<!-- vim-markdown-toc -->

## 1.概述

- session存储在服务器端(内存)，`依赖于cookie`，通常根据`存在cookie中的session id`(可以经过算法加密)来找到对应的session
- 每次验证的用户发送请求时，服务器储存信息，导致占用过多资源，同时`可扩展性也不强`
- 两种实现方式：`1.将session的id存在cookie里；2.使用url重写的方式，可以在url中嵌入session id`
- session的有效过期时间需要配置,默认有效时间为30分钟
