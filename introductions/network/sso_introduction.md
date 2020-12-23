# SSO介绍

<!-- vim-markdown-toc Marked -->

* [1.概念](#1.概念)
* [2.技术实现](#2.技术实现)
        - [2.1同域下的SSO(不是真正的SSO)](#2.1同域下的sso(不是真正的sso))
        - [2.2CAS](#2.2cas)
        - [2.3不同域下的SSO](#2.3不同域下的sso)

<!-- vim-markdown-toc -->

## 1.概念

- [参考文章](https://www.jianshu.com/p/75edcc05acfd)
- `SSO(single sign on)`, 单点登录，在多个应用系统中，只需要登录一次，就可以访问其他相互信任的应用系统
- Cookie是不能跨域的，我们Cookie的domain属性是sso.a.com，在给app1.a.com和app2.a.com发送请求是带不上的
- 不同的应用，它们的session存在自己的应用内，是不共享的。

## 2.技术实现

### 2.1同域下的SSO(不是真正的SSO)

1. 域名: a.com, 应用1: app1.a.com, 应用2: app2.a.com, 单点登录应用: sso.a.com
2. sso登录之后，将cookie的域设置为`顶域`,即a.com, 这样其他的应用也能用到该cookie
3. 根据该cookie可以通过`共享session`，实现其他应用的登录

### 2.2CAS

- [官网](https://apereo.github.io/cas/5.1.x/)

### 2.3不同域下的SSO
