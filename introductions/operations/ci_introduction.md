# CI持续集成(Continuous integration)

<!-- vim-markdown-toc Marked -->

* [1.概念](#1.概念)
* [持续交付(Continuous delivery)](#持续交付(continuous-delivery))
* [持续部署](#持续部署)
* [测试](#测试)
* [TDD测试驱动开发(Test Driven Development)](#tdd测试驱动开发(test-driven-development))

<!-- vim-markdown-toc -->

## 1.概念

频繁将代码集成到主干,目的是让产品可以快速迭代，同时还能保持高质量。
核心措施是：代码集成到主干之前，必须通过自动化测试。只要有一个测试用例失败，就不能集成。

优势:

1. 提高开发效率
2. 快速发现并定位bug
3. 快速的发布更新

## 持续交付(Continuous delivery)

频繁地将软件的新版本，交付给质量团队或者用户，以供评审。如果评审通过，代码就进入生产阶段。

## 持续部署

代码通过评审以后，自动部署到生产环境。

## 测试

`单元测试`：针对函数或模块的测试。
`集成测试`：针对整体产品的某个功能的测试，又称功能测试。
`端对端测试`：从用户界面直达数据库的全链路测试。

[python unittest的详细介绍使用](http://c.biancheng.net/view/2679.html)

## TDD测试驱动开发(Test Driven Development)

TDD是一种敏捷开发方式，而不是测试方法。

- [参考博客](https://blog.csdn.net/weixin_41845533/article/details/81232812)
