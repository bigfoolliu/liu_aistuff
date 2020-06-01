# Git

<!-- vim-markdown-toc Marked -->

* [1.git基本命令](#1.git基本命令)
        * [1.1配置(config)](#1.1配置(config))
        * [1.2仓库克隆(clone)](#1.2仓库克隆(clone))
        * [1.3暂存(add)](#1.3暂存(add))
        * [1.4本地提交(commit)](#1.4本地提交(commit))
        * [1.5远程提交于拉取(push, pull)](#1.5远程提交于拉取(push,-pull))
        * [1.6提交堆栈(stash)](#1.6提交堆栈(stash))
        * [1.7分支(branch)](#1.7分支(branch))
        * [1.8撤销(reset, revert)](#1.8撤销(reset,-revert))
        * [1.9操作记录(log, reflog)](#1.9操作记录(log,-reflog))
        * [1.10标签(tag)](#1.10标签(tag))
        * [1.11查看内容(show)](#1.11查看内容(show))
        * [1.12状态(status)](#1.12状态(status))
        * [1.x其他(diff)](#1.x其他(diff))
* [2.操作命令组](#2.操作命令组)
        * [2.1修改已经push的commit的message](#2.1修改已经push的commit的message)
        * [2.2修改多次commit的信息为一个](#2.2修改多次commit的信息为一个)
        * [2.3提交之后因为大文件而push失败](#2.3提交之后因为大文件而push失败)
* [3..gitignore文件](#3..gitignore文件)
        * [3.1介绍](#3.1介绍)
        * [3.2格式规范](#3.2格式规范)
* [4.gitmoduel使用](#4.gitmoduel使用)
* [4.其他](#4.其他)
        * [4.非常用命令](#4.非常用命令)
        * [4.2github搜索技巧](#4.2github搜索技巧)

<!-- vim-markdown-toc -->

## 1.git基本命令

### 1.1配置(config)

```shell
# 一般配置
# 查看版本信息
git --version

# 获取全局登陆的用户,邮箱
git config --global user.name
git config --global user.email


# 获取某个仓库的用户和邮箱(需要进入该仓库)
git config --local user.name
git config --local user.email

# 查看所有的配置以及配置文件所在的位置
git config --list --show-origin
# 查看当前所有的git能找到的配置
git config --list

# 直接进入编辑全局配置文件
git config -e --global

# 登陆git
# 设置全局git账户
git config --global user.name "userName"
git config --global user.email "userEmail"

# 设置单个仓库的git账户
git config --local user.name "userName"
git conig --local user.email "userEmail"


# 将git的文本编辑器修改为vim
git config --global core.editor vim
```

### 1.2仓库克隆(clone)

```shell
# 从远程克隆一个版本库
git clone `address`
```

### 1.3暂存(add)

```shell
# 将所有修改文件暂存
git add .

# 将指定文件暂存
git add test.py
```

### 1.4本地提交(commit)

```shell
# 直接提交
git commit

# 带注释的提交
git commit -m "init"

# 提交当前repo的所有改变，可以跳过git add(慎用，可能会添加不需要的文件)
git commit -a -m "format"

# 修改上一次提交的信息
git commit --amend
```

### 1.5远程提交于拉取(push, pull)

```shell
# 当前分支只有一个追踪分支，直接将本地的分支的更新推送至远程主机
git push
git push <远程主机名>　<本地分支名>:<远程分支名>
git push origin master:master  # 将本地的master分支推送到远程的master分支
git push origin master:dev  # 将本地的master分支推送到远程的dev分支


# 当前分支只有一个追踪分支，直接取回远程主机某个分支的更新，与本地的分支合并
git pull
# 与本地的指定合并
git pull <远程主机名>　<远程分支名>:<本地分支名>

# 强制推到远程(慎用)
git push -f
```

### 1.6提交堆栈(stash)

- [git stash clear之后如何找回数据](https://www.jianshu.com/p/3c2292223335)

```shell

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

# 删除存储堆栈中指定的进度
git stash drop stash@{0}

# 删除所有存储的进度
git stash clear

# 将当前stash中的内容应用到当前分支对应的工作目录（不会删除堆栈中最近保存的内容）
git stash apply

# 使用指定的堆栈中的内容
git stash apply stash@{0}

# 查看某个堆栈中的修改内容
git stash show -p stash@{0}
```

### 1.7分支(branch)

```shell
# 取回所有分支的更新
git fetch
# 取回指定的分支更新(eg:git fetch origin master)
git fetch <远程主机名> <分支名>

# 切换到本地的dev分支
git checkout dev

# 建立一个新的本地dev分支
git checkout -b dev

# 导航到之前的一个分支
git checkout -


# 查询本地仓库，远程仓库，跟踪关系最全的命令
git branch -vv -a

# 删除本地分支
git branch -d dev

# 删除远程分支
git push origin --delete dev

# 获取远程仓库的地址
git remote get-url origin
```

### 1.8撤销(reset, revert)

```shell
# reset撤销直接删除指定的commit,将HEAD后移
# 撤销对所有文件的暂存
git reset HEAD

# 撤销对指定文件的暂存
git reset HEAD test.py


# revert会将操作之前和之后的信息都会保留,用新的commit回滚旧的commit
# 撤销前一次commit
git revert HEAD

# 撤销前前一次commit
git revert HEAD^

# 撤销指定的版本
git revert commit d92761fec08ecca646f81402a415e9a07f9638b6
```

### 1.9操作记录(log, reflog)

- git reflog是显示所有的操作记录，包括提交，回退的操作。一般用来找出操作记录中的版本号，进行回退
- git reflog常用于恢复本地的错误操作

```shell
# 查看提交历史
git log

# 查看提交历史并显示每次提交的差异
git log -p
git log -p -2  # 只查看最近的两次提交

# 每次提交的简略统计信息，加减行数
git log --stat

# 带简单ascii字符来图形化展示
git log --graph

# 筛选作者
git log --author=bigfoolliu

# 查看所有的操作记录
git reflog show

# 查看分支操作记录
git reflog master
```

### 1.10标签(tag)

- 软件发布的时候通常使用，会记录版本的commit号,方便回溯
- 一般的打tag都是建立在head上

```shell
# 查看目前已经打上的标签
git tag

# 显示tag，并通过关键字过滤
git tag -l "v1"

# 直接创建一个tag
git tag v1.0

# 创建一个带备注信息的tag
git tag -a v1.0 -m "有备注信息的tag"

# 在某一个提交对象上打tag，只要提交对象的校验和前几位
git tag -a v1.0 9fedamdch -m "有备注信息的tag"

# tag创建完成之后，也需要推送到远程
# 推送单个tag
git push origin v1.0

# 推送所有的tag
git push origin --tags


# 删除本地的tag
git tag -d v1.0

# 删除远程的tag
git push origin :refs/tags/v1.0
```

### 1.11查看内容(show)

```shell
# 查看tag的详细信息
git show v1.0


# 查看某次提交的内容
git show <commit_id>
# 查看某次提交的某个文件的修改
git show <commit_id> <file_name>
```

### 1.12状态(status)

```shell
# 检查当前文件状态
git status

# 以更简短的方式检查文件状态
git status -s
```

### 1.x其他(diff)

```shell
# 查看暂未暂存的文件更新哪些部分
git diff


```

## 2.操作命令组

### 2.1修改已经push的commit的message

- [已经push的commit如何修改message](https://www.jianshu.com/p/ec45ce13289f)

```shell
# 1.确定修改哪些commit
git rebase -i HEAD~5

# 2.在vim中将待修改的commit的 pick 改为 edit，然后保存退出，此时git的分支发生改变，改成了我们第一个edit的commit id
# 3.在当前分支轮流执行（有几条message要修改就执行几次）以下两个命令,执行完第一个命令，修改message保存
git commit --amend
git rebase --continue
```

### 2.2修改多次commit的信息为一个

```shell
# 定位到指定的commit，修改cmmmit的message，倒数的修改为`squash`
git rebase -i <commid_id>
# 修改掉多余的commit message
git rebase --continue
```

### 2.3提交之后因为大文件而push失败

```shell
# 回退至指定的版本号
git reset --hard `commit_id`
# 远程提交回退
git push origin HEAD --force
# 删除缓存
git rm -r --cached .
```

## 3..gitignore文件

### 3.1介绍

- 子目录中也可以有额外的.gitignore文件，且只应用到子目录
- [常用.gitignore文件](https://github.com/github/gitignore)
- [自动生成.gitignore文件网站](https://gitignore.io/)

### 3.2格式规范

- 所有空行或者以 # 开头的行都会被 Git 忽略。
- 可以使用标准的 glob 模式匹配，它会递归地应用在整个工作区中。
- 匹配模式可以以(/)开头防止递归。
- 匹配模式可以以(/)结尾指定目录。
- 要忽略指定模式以外的文件或目录，可以在模式前加上叹号(!)取反。

glob 模式是指 shell 所使用的简化了的正则表达式。 星号(*)匹配零个或多个任意字符;[abc] 匹配 任何一个列在方括号中的字符 (这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c); 问号(?)只 匹配一个任意字符;如果在方括号中使用短划线分隔两个字符， 表示所有在这两个字符范围内的都可以匹配 (比如 [0-9] 表示匹配所有 0 到 9 的数字)。 使用两个星号(**)表示匹配任意中间目录，比如 a/**/z 可以 匹配 a/z 、 a/b/z 或 a/b/c/z 等。

## 4.gitmoduel使用

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
```

```shell
# 初始化本地.gitmodules文件
git submodule init
# 同步远端submodule源码
git submodule update
# 给一个仓库添加子仓库
git submodule add <submodule_url>
# 获取主项目和所有子项目源码
git clone --recurse-submodules <main_project_url>

# 删除子模块
rm -rf <submodule dir>  # 删除子模块的目录以及源码
vim .gitmodule  # 删除项目目录下.gitmodule文件中子模块相关条目
vim .git/config  # 删除配置中子模块相关条目
rm .git/module/*  # 删除模块下的子模块目录
git rm --cached  <submodule name>  # 如果执行完成之后报错执行
```

## 4.其他

### 4.非常用命令

```shell
# 查看当前状态
git status

# 查看commit的日志
git log
# 每个提交在一行显示，更加清晰
git log --oneline
# 获取某人的提交的日志
git log --author="tony"
# 在所有提交中搜索包含关键字的提交
git log --all --grep="homepage"
# 指定时间范围内的查询
git log --author="liurui" --after="2020-01-01 00:00:00" --before="2020-04-01 00:00:00"

# 获取所有操作历史
git reflog

# 查看尚未暂存的更新
git diff
# 查看尚未提交的更新
git diff --cached
```

**pull request:**

- fork仓库后修改了错误，然后给原始仓库提交`pull request`
- 原仓库的所有者看到`pr`,进行`review`，觉得对的就`merge`,完成流程

**index文件损坏处理:**

```shell
rm -rf .git/index
git reset --mixed HEAD
```

**错误的commit并提交到远程**

```shell
git log
git reset --soft HEAD~2  # 不删除工作空间改动代码，撤销commit，不撤销git add . 或者将HEAD~2改为回退到的版本号
git push origin 分支名 --force  # 将当前撤销的提交推送到远程
```

### 4.2github搜索技巧

```shell
# 名字包含python，stars数量大于1000
python in:name stars:>1000

in:readme 

in:description

language:python

pushed:2020-01-01
```

