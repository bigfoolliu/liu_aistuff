# git相关知识

<!-- TOC -->

- [git相关知识](#git%e7%9b%b8%e5%85%b3%e7%9f%a5%e8%af%86)
  - [1.git基本命令](#1git%e5%9f%ba%e6%9c%ac%e5%91%bd%e4%bb%a4)
  - [2.其他相关操作](#2%e5%85%b6%e4%bb%96%e7%9b%b8%e5%85%b3%e6%93%8d%e4%bd%9c)
    - [2.1修改已经push的commit的message](#21%e4%bf%ae%e6%94%b9%e5%b7%b2%e7%bb%8fpush%e7%9a%84commit%e7%9a%84message)
    - [2.2修改多次commit的信息为一个](#22%e4%bf%ae%e6%94%b9%e5%a4%9a%e6%ac%a1commit%e7%9a%84%e4%bf%a1%e6%81%af%e4%b8%ba%e4%b8%80%e4%b8%aa)
  - [3.gitmoduel使用](#3gitmoduel%e4%bd%bf%e7%94%a8)

<!-- /TOC -->

## 1.git基本命令

```shell
# 一般配置
# 查看版本信息
git --version
# 获取当前登陆的用户
git config --global user.name
# 获取当前登陆用户的邮箱
git config --global user.email

# 登陆git:
# 设置git账户，userName为用户名
git config --global user.name `userName`
git config --global user.email `userEmail>`
# 将git的文本编辑器修改为vim
git config --global core.editor vim

# 从远程克隆一个版本库
git clone `address`

# 查看当前状态
git status

# 将所有修改文件暂存
git add .
# 将指定文件暂存
git add test.py

# 撤销对所有文件的暂存
git reset HEAD
# 撤销对指定文件的暂存
git reset HEAD test.py

# 直接提交
git commit
# 带注释的提交
git commit -m `message`
# 提交当前repo的所有改变
git commit -a
# 移除文件(从Git中删除)
git commit -m "remove"
# 修改上一次提交的信息
git commit --amend

# 当前分支只有一个追踪分支，直接将本地的分支的更新推送至远程主机
git push
git push <远程主机名>　<本地分支名>:<远程分支名>

# 当前分支只有一个追踪分支，直接取回远程主机某个分支的更新，与本地的分支合并
git pull
# 与本地的指定合并
git pull <远程主机名>　<远程分支名>:<本地分支名>

# 当前分支内容修改了，但是还不想提交，此时需要切换到另一个分支，则该命令将当前分支修改的内容
# 保存到堆栈中，然后就可以在不同的分支中进行切换了
# 将所有未提交的修改（工作区和暂存区）保存到堆栈
git stash
# 等同于stash,但是可以加一些注释
git stash save "message"
# 查看当前stash中内容
git stash list
# 将当前stash中的内容弹出，并应用到当前分支对应的工作目录（会删除堆栈中最近保存的内容）
git stash pop
# 将当前stash中的内容应用到当前分支对应的工作目录（不会删除堆栈中最近保存的内容）
git stash apply
# 删除所有存储的进度
git stash clear

# 取回所有分支的更新
git fetch
# 取回指定的分支更新(eg:git fetch origin master)
git fetch <远程主机名> <分支名>

# 查看commit的日志
git log

# 查看尚未暂存的更新
git diff
# 查看尚未提交的更新
git diff --cached

# 切换到本地的dev分支
git checkout `dev`
# 建立一个新的本地dev分支
git checkout -b `dev`

# 直接进步编辑全局配置文件
git config -e --global

# 当文件提交comnit后push因为大文件而失败
# 回退至指定的版本号
git reset --hard `commit_id`
# 远程提交回退
git push origin HEAD --force
# 删除缓存
git rm -r --cached .

# 初始化本地.gitmodules文件
git submodule init
# 同步远端submodule源码
git submodule update
# 给一个仓库添加子仓库
git submodule add <submodule_url>
# 获取主项目和所有子项目源码
git clone --recurse-submodules <main_project_url>

# 获取远程仓库的地址
git remote get-url origin
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

### 2.2修改多次commit的信息为一个

```shell
# 定位到指定的commit，修改cmmmit的message，倒数的修改为`squash`
git rebase -i <commid_id>
# 修改掉多余的commit message
git rebase --continue
```

## 3.gitmoduel使用

gitsubmodule是多项目使用共同类库的工具。

```shell
# 增加submodule
# 父repo增加submodule的repo
git submodule add http://github.com/bigfooliu/liu_work.git

# 修改submodule,首先Push submodule的变动，然后Push父repo的变动
cd liu_work
git add
git commit
git push
cd ..
git push

# 更新submodule,两种方式
git submodule foreach git pull  # 直接父repo
cd liu_work  # 进入submodule
git pull

# clone submodule
# 采用递归的方式clone整个项目,父项目和submodule
git clone git@xxx.git --recursive

# 删除submodule,需要手动删除文件
git rm --cached liu_work
rm -rf liu_work
rm .gitmodules
# 然后重新提交修改信息
````
