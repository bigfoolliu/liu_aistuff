# git相关知识

<!-- TOC -->

- [git相关知识](#git%e7%9b%b8%e5%85%b3%e7%9f%a5%e8%af%86)
  - [1.git基本命令](#1git%e5%9f%ba%e6%9c%ac%e5%91%bd%e4%bb%a4)
  - [2.其他相关操作](#2%e5%85%b6%e4%bb%96%e7%9b%b8%e5%85%b3%e6%93%8d%e4%bd%9c)
    - [2.1修改已经push的commit的message](#21%e4%bf%ae%e6%94%b9%e5%b7%b2%e7%bb%8fpush%e7%9a%84commit%e7%9a%84message)

<!-- /TOC -->

## 1.git基本命令

```shell
# 一般配置

git --version       查看版本信息
git config --global user.name       获取当前登陆的用户
git config --global user.email      获取当前登陆用户的邮箱

# 登陆git:

git config --global user.name `userName`      设置git账户，userName为用户名
git config --global user.email `userEmail>`
git config --global core.editor vim     将git的文本编辑器修改为vim

git clone `address`     从远程克隆一个版本库

git status      查看当前状态

git commit      直接提交
git commit -m `message`       带注释的提交
git commit -a       提交当前repo的所有改变
git commit -m "remove"      移除文件(从Git中删除)

git push        当前分支只有一个追踪分支，直接将本地的分支的更新推送至远程主机
git push <远程主机名>　<本地分支名>:<远程分支名>

git pull        当前分支只有一个追踪分支，直接取回远程主机某个分支的更新，与本地的分支合并
git pull <远程主机名>　<远程分支名>:<本地分支名>        与本地的指定合并

git fetch       取回所有分支的更新
git fetch <远程主机名> <分支名>     取回指定的分支更新(eg:git fetch origin master)

git log     查看commit的日志

git diff        查看尚未暂存的更新
git diff --cached       查看尚未提交的更新

git checkout `dev`      切换到本地的dev分支
git checkout -b `dev`       建立一个新的本地dev分支

git config -e --global      直接进步编辑全局配置文件

当文件提交comnit后push因为大文件而失败:
git reset `id`　　回退至指定的版本号
git rm -r --cached .　　删除缓存

git submodule init  初始化本地.gitmodules文件
git submodule update    同步远端submodule源码
git submodule add <submodule_url>   给一个仓库添加子仓库
git clone --recurse-submodules <main_project_url>   获取主项目和所有子项目源码

git remote get-url origin   获取远程仓库的地址
```

## 2.其他相关操作

### 2.1修改已经push的commit的message

[已经push的commit如何修改message](https://www.jianshu.com/p/ec45ce13289f)

```shell
# 1.确定修改哪些commit
git rebase -i HEAD~5

# 2.在vim中将待修改的commit的 pick 改为 edit，然后保存退出，此时git的分支发生改变，改成了我们第一个edit的commit id
# 3.在当前分支轮流执行（有几条message要修改就执行几次）以下两个命令,执行完第一个命令，修改message保存
git commit --amend
git rebase --continue

# 4.强制推到远程
git push -f
```
