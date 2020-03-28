# 编码设计相关规范

<!-- TOC -->

- [编码设计相关规范](#%e7%bc%96%e7%a0%81%e8%ae%be%e8%ae%a1%e7%9b%b8%e5%85%b3%e8%a7%84%e8%8c%83)
  - [1.shell](#1shell)
    - [1.1参考](#11%e5%8f%82%e8%80%83)
    - [1.2background](#12background)
    - [1.3environment](#13environment)
    - [1.4comments](#14comments)
    - [1.5formatting](#15formatting)
  - [2.http-api设计规范](#2http-api%e8%ae%be%e8%ae%a1%e8%a7%84%e8%8c%83)
    - [2.1参考](#21%e5%8f%82%e8%80%83)
  - [3.开发和部署规范](#3%e5%bc%80%e5%8f%91%e5%92%8c%e9%83%a8%e7%bd%b2%e8%a7%84%e8%8c%83)
    - [3.1参考](#31%e5%8f%82%e8%80%83)
    - [3.2](#32)

<!-- /TOC -->

来源：[github编码规范](https://github.com/NARKOZ/guides)

## 1.shell

### 1.1参考

- [google shell规范](https://google.github.io/styleguide/shell.xml)

### 1.2background

- 可执行的shell必须以`#!/bin/bash`开头
- shell应该是用于小型的实用程序或简单的包装器脚本
- 代码量尽量不超过100行
- 可执行文件不要有`.sh`扩展，库则必须要有扩展且不可执行

### 1.3environment

- 所有的错误信息到`STDERR`

### 1.4comments

- 所有的文件需要有简单的介绍以及版权信息和作者信息(可选)
- 任何库中的函数都应该有注释 
- 使用`TODO`注释来申明代码是临时的

### 1.5formatting

- 缩进使用2空格，不要使用tab
- 单行不超过80个字符
- 管道尽量分开到不同的行
- 将`: do`和`: then`放到`while, for, if`的同一行
- 变量使用时候，尽量使用`${var}`，而不是`$var`

## 2.http-api设计规范

### 2.1参考

- [http api设计规范参考](https://devcenter.heroku.com/articles/platform-api-reference)
- [http api设计规范参考](https://geemus.gitbooks.io/http-api-design/content/en/requests/actions.html)

## 3.开发和部署规范

### 3.1参考

- [分支开发规范](http://guides.beanstalkapp.com/version-control/branching-best-practices.html)
- [环境规范](http://guides.beanstalkapp.com/deployments/best-practices.html)

### 3.2

## 4.git提交信息规范

### 4.1commit格式参考

- [阮一峰 git commit message和change log编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)
- [wiki gitlab提交规范](https://wiki.hcmcloud.cn/pages/viewpage.action?pageId=18416313)

### 4.2commit格式示例

**commit message格式:**

```shell
<type>(<scope>):<subject>

<body>

<footer>
```

其中:

header包含三个部分: type(必需),scope(可选),subject(必需)

`type`的类型可选::

1. feat(新功能)
2. fix(修补bug)
3. docs(文档)
4. style(格式)
5. refactor(重构,不是新增功能,也不是修改bug的变动)
6. test(增加测试)
7. chore(构建过程或者辅助工具的变动)

*当type为feat或者fix时候,commit肯定出现在change log中,其他类型则可选.*

`scope`说明影响的范围,如数据层,模型层,控制层等,取决于项目,如`model`.

`subject`是commit目的的简短描述,如`修改person为Person`.

`body`是对本次commit的详细描述,可以分成多行.

`footer`用于两种情况:

1. 不兼容变动,即当前代码和上一个版本不兼容,格式为:`BREAKING CHANGE:`,后跟变动的描述,以及变动理由和迁移方法
2. 关闭issaue,如`close #123`

**commit为revert撤销操作的时候:**

以`revert:`为开头,后面跟着被撤销commit的header,如:`revert: feat(model): add something this revert commit d92761fec08ecca646f81402a415e9a07f9638b6`.

