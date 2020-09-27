# maven介绍

<!-- vim-markdown-toc Marked -->

* [1.安装使用](#1.安装使用)
        - [1.1仓库](#1.1仓库)
* [2.命令](#2.命令)

<!-- vim-markdown-toc -->

## 1.安装使用

- 一款帮助构建项目的工具
- 告诉Maven需要哪些Jar 包，它会帮助我们下载所有的Jar，极大提升开发效率

### 1.1仓库

- **本地仓库**, Maven本地的Jar包仓库
- **中央仓库**, Maven官方提供的远程仓库
- 当项目编译时，Maven首先从本地仓库中寻找项目所需的Jar包，若本地仓库没有，再到Maven的中央仓库下载所需Jar包

## 2.命令

```sh
# 查看基本信息
mvn -v

# 将java源文件编译为class文件
mvn compile

# 测试项目
mvn test

# 将项目打包为jar包
mvn package

# 删除target文件夹
mvn clean

# 将当前项目放到Maven的本地仓库中,供其他项目使用
mvn install
```
