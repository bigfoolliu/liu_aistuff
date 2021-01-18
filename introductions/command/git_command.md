# Git

## 1.git基本命令

<!-- vim-markdown-toc Marked -->

* [1.基础命令](#1.基础命令)
    - [1.1配置(config)](#1.1配置(config))
    - [1.2仓库初始化或克隆(clone)](#1.2仓库初始化或克隆(clone))
    - [1.3暂存(add)](#1.3暂存(add))
    - [1.4本地提交(commit)](#1.4本地提交(commit))
    - [1.5远程提交于拉取(push, pull)](#1.5远程提交于拉取(push,-pull))
    - [1.6提交堆栈(stash)](#1.6提交堆栈(stash))
    - [1.7分支(fetch, branch, checkout)](#1.7分支(fetch,-branch,-checkout))
    - [1.8撤销(reset, revert)](#1.8撤销(reset,-revert))
    - [1.9操作记录(log, reflog)](#1.9操作记录(log,-reflog))
    - [1.10标签(tag)](#1.10标签(tag))
    - [1.11查看内容(show)](#1.11查看内容(show))
    - [1.12状态(status)](#1.12状态(status))
    - [1.13删除(rm)](#1.13删除(rm))
    - [1.14移动(mv)](#1.14移动(mv))
    - [1.15查看更新(diff)](#1.15查看更新(diff))
    - [1.16远程(remote)](#1.16远程(remote))
    - [1.17清除(clean)](#1.17清除(clean))
* [2.操作命令组](#2.操作命令组)
    - [2.1修改已经push的commit的message](#2.1修改已经push的commit的message)
    - [2.2修改多次commit的信息为一个](#2.2修改多次commit的信息为一个)
    - [2.3提交之后因为大文件而push失败](#2.3提交之后因为大文件而push失败)
    - [2.4提交错误且已经push到远程](#2.4提交错误且已经push到远程)
* [3.gitignore文件](#3.gitignore文件)
    - [3.1介绍](#3.1介绍)
    - [3.2格式规范](#3.2格式规范)
* [4.gitmodule](#4.gitmodule)
    - [4.1介绍](#4.1介绍)
    - [4.2使用](#4.2使用)
* [5.其他](#5.其他)
    - [5.1非常用命令](#5.1非常用命令)
    - [5.2github](#5.2github)
        + [5.2.1github搜索技巧](#5.2.1github搜索技巧)
        + [5.2.2github知识](#5.2.2github知识)
    - [5.3在服务器上搭建git](#5.3在服务器上搭建git)
    - [5.4如何选择git的分支模式](#5.4如何选择git的分支模式)
        + [5.4.1TBD](#5.4.1tbd)
        + [5.4.2Git-Flow模式](#5.4.2git-flow模式)
        + [5.4.3Github-Flow模式](#5.4.3github-flow模式)
        + [5.4.4Gitlab-Flow模式](#5.4.4gitlab-flow模式)
    - [5.5git-lfs使用](#5.5git-lfs使用)
        + [5.5.1概述](#5.5.1概述)
        + [5.5.2使用](#5.5.2使用)

<!-- vim-markdown-toc -->

## 1.基础命令

- ![git仓库以及命令关系](./imgs/git_repo_intro.jpg)

### 1.1配置(config)

```sh
# 一般配置
# 查看版本信息
git --version

# 获取全局登陆的用户,邮箱
git config --global "user.name"
git config --global "user.email"

# 设置启动的编辑器
git config --global core.editor vim
git config --global core.editor emacs

# 获取某个仓库的用户和邮箱(需要进入该仓库)
git config --local user.name
git config --local user.email

git config --list --show-origin  # 查看所有的配置以及配置文件所在的位置
git config --list  # 查看当前所有的git能找到的配置

git config -e --global  # 直接进入编辑全局配置文件

git config --global alias.ci commit  # 设置别名,commit别名为ci, 则git ci来替代git commit

# 设置单个仓库的git账户
git config --local user.name "userName"
git config --local user.email "userEmail"

# 当不能显示中文的时候
git config --global core.quotepath false
```

### 1.2仓库初始化或克隆(clone)

git可以使用四种不同的协议来传输数据：

1. 本地协议(Local): `git clone /srv/git/project.git`或者`git clone file:///srv/git/project.git`
2. HTTP协议：`git clone https://xxx.com/xxx.git`
3. SSH协议：`git clone ssh://[user@]server/project.git]`
4. Git协议

```sh
# 1.初始化
git init repo   # 创建一个git仓库，有.git目录，不能推送修改到“非裸仓库”
git init --bare repo.git  # 创建一个裸库，没有.git目录，没有工作区（不能在仓库里进行git操作），只会记录git提交的历史信息，裸仓库一般情况下仅作为远程仓库使用，主要是为了维护远程的仓库的“干净”

# 2.克隆
git clone <git_address>  # 从远程克隆一个版本库
git clone --depth 1 <git_address>  # 浅克隆，不要commit历史，只要代码
```

### 1.3暂存(add)

- 由于git commit的操作是原子性的,如果本次commit的内容没有完成，却要切换至其他分支等操作，那么可以将其暂存

```sh
git add .  # 将所有修改文件暂存
git add test.py  # 将指定文件暂存
git add -i  # 使用交互式的暂存
```

### 1.4本地提交(commit)

- git commit在提交信息中换行，只需要单引号，且换行之后再补齐另一半单引号即可

```sh
git commit  # 直接提交
git commit -m "init"  # 带注释的提交
git commit -m "line1" -m "line2"  # 带注释的提交,可以有多个-m,表示多行
git commit -a -m "format"  # 提交当前repo的所有改变，可以跳过git add(慎用，可能会添加不需要的文件)

# 1. 如果上次提交以来修改了，会将暂存区中的文件提交,从而将本次的修改合并到上一次的提交(适用于一次提交忘了提交某些信息的场景)
# 2. 如果上次提交以来没有任何修改，则只是修改上一次提交的信息(适用于修改提交信息的场景)
git commit --amend -m [message]
```

### 1.5远程提交于拉取(push, pull)

```sh
# 当前分支只有一个追踪分支，直接将本地的分支的更新推送至远程主机
git push
git push <远程主机名>　<本地分支名>:<远程分支名>
git push origin master:master  # 将本地的master分支推送到远程的master分支
git push origin master:dev  # 将本地的master分支推送到远程的dev分支

git pull  # 当前分支只有一个追踪分支，直接取回远程主机某个分支的更新，与本地的分支合并
git pull <远程主机名>　<远程分支名>:<本地分支名>  # 与本地的指定合并


git push -f  # 强制推到远程(慎用)
```

### 1.6提交堆栈(stash)

- [git stash clear之后如何找回数据](https://www.jianshu.com/p/3c2292223335)

```sh
# 当前分支内容修改了，但是还不想提交，此时需要切换到另一个分支，则该命令将当前分支修改的内容
# 保存到堆栈中，然后就可以在不同的分支中进行切换了
# 将所有未提交的修改（工作区和暂存区）保存到堆栈
git stash

git stash save "message"  # 等同于stash,但是可以加一些注释
git stash list  # 查看当前stash中内容
git stash pop  # 将当前stash中的内容弹出，并应用到当前分支对应的工作目录（会删除堆栈中最近保存的内容）
git stash drop stash@{0}  # 删除存储堆栈中指定的进度
git stash clear  # 删除所有存储的进度
git stash apply  # 将当前stash中的内容应用到当前分支对应的工作目录（不会删除堆栈中最近保存的内容）
git stash apply stash@{0}  # 使用指定的堆栈中的内容
git stash show -p stash@{1}  # 查看某个堆栈中的修改内容
git stash show -p  # 查看最近一个stash里面的修改
```

### 1.7分支(fetch, branch, checkout)

- 特殊指针HEAD，用来指向当前所处的本地分支

```sh
git fetch  # 取回所有分支的更新
git fetch <远程主机名> <分支名>  # 取回指定的分支更新(eg:git fetch origin master)
git fetch -p # 跟随远程删除分支的操作删除本地分支
git fetch -P # 跟随远程删除分支的操作删除本地tag

git checkout a.txt  # 取消对某个文件的修改(即没有文件),恢复暂存区的指定文件到工作区
git checkout [commit] [file]  # 恢复某个commit的指定文件到工作区
git checkout dev  # 切换到本地的dev分支
git checkout -b dev  # 建立一个新的本地dev分支并切换到该分支
git checkout -  # 导航到之前的一个分支

git branch  # 查看本地所有分支
git branch -v  # 查看本地所有分支和分支的最后一次提交
git branch -vv -a  # 查询本地仓库，远程仓库，跟踪关系最全的命令
git branch -d dev  # 删除本地分支
git branch --merged  # 查看本地已经合并到当前的分支
git branch --no-merged  # 查看本地还没有合并到当前的分支

git push origin --delete dev  # 删除远程分支

git remote get-url origin  # 获取远程仓库的地址
```

### 1.8撤销(reset, revert)

- reset撤销直接删除指定的commit, 将HEAD后移
- revert会将操作之前和之后的信息都会保留, 用新的commit回滚旧的commit

```sh
git reset HEAD  # 撤销对所有文件的暂存, add到暂存区的代码想撤销
git reset HEAD test.py  # 撤销对指定文件的暂存(适用于误将文件暂存add的场景)
git reset HEAD~1  # 如果想要将一个分支的最后一个提交转移到另外一个分支,然后git stash，应用到另外一个分支

git reset --soft HEAD~1  # 将刚刚的提交撤回到暂存区
git reset --soft HEAD^  # 将刚刚的提交撤回到暂存区
git reset --soft HEAD~3  # 撤销最近的三次提交，HEAD, HEAD^ 和HEAD~2均被撤销

git reset --hard <commit_id/版本号>  # 提交到本地仓库的代码想撤销

git revert HEAD  # 撤销前一次commit
git revert HEAD^  # 撤销前前一次commit
git revert commit d92761fec08ecca646f81402a415e9a07f9638b6  # 撤销指定的版本
```

### 1.9操作记录(log, reflog)

- git reflog是显示所有的操作记录，包括提交，回退的操作。一般用来找出操作记录中的版本号，进行回退
- git reflog常用于恢复本地的错误操作

```sh
git log  # 查看提交历史

git log -p  # 查看提交历史并显示每次提交的差异
git log -p -2  # 只查看最近的两次提交
git log -p <file_name>  # 查看某个文件每次提交的diff

git log --stat  # 每次提交的简略统计信息，加减行数
git log --graph  # 带简单ascii字符来图形化展示
git log --author=bigfoolliu  # 筛选作者
git log --grep content  # 模糊搜索
git log --pretty=format:"%H - %an, %cd : %s"  # 使用特定的格式输出log

# %H 提交的完整哈希值
# %h 提交的简写哈希值
# %T 树的完整哈希值
# %t 树的简写哈希值
# %P 父提交的完整哈希值
# %p 父提交的简写哈希值
# %an 作者名字
# %ae 作者的电子邮件地址
# %ad 作者修订日期(可以用 --date=选项 来定制格式)
# %ar 作者修订日期，按多久以前的方式显示
# %cn 提交者的名字
# %ce 提交者的电子邮件地址
# %cd 提交日期
# %cr 提交日期(距今多长时间)
# %s 提交说明


git reflog show  # 查看所有的操作记录
git reflog master  # 查看分支操作记录
git reflog --date=local | grep branch_name  # 查看branch_name分支是基于哪个分支创建的
```

### 1.10标签(tag)

- 软件发布的时候通常使用，会记录版本的commit号,方便回溯
- 一般的打tag都是建立在head上

```sh
git tag  # 查看目前已经打上的标签
git tag -l "v1"  # 显示tag，并通过关键字过滤

git tag v1.0  # 直接创建一个tag
git tag -a v1.0 -m "有备注信息的tag"  # 创建一个带备注信息的tag
git tag -a v1.0 <commit_id> -m "有备注信息的tag"  # 在某一个提交对象上打tag，只要提交对象的校验和前几位

# tag创建完成之后，需要单独推送到远程,如果
# 推送单个tag
git push origin v1.0

# 推送所有的tag
git push origin --tags

# 删除tag
git tag -d v1.0  # 删除本地的tag
git push origin :refs/tags/v1.0  # 将冒号之前的空值推动到远程的tag从而删除远程的tag
git push origin --delete v1.0  # 更直观的删除远程标签
```

### 1.11查看内容(show)

```sh
git show  # 查看最近的commit
git show v1.0  # 查看tag的详细信息
git show <commit_id>  # 查看某次提交的内容

git show <commit_id> <file_name>  # 查看某次提交的某个文件的修改
```

### 1.12状态(status)

```sh
git status  # 检查当前文件状态
git status -s  # 以更简短的方式检查文件状态
```

### 1.13删除(rm)

- git移除文件,需要从暂存区中删除，然后提交
- 如果直接删除已经暂存的文件，需要再次提交

```sh
# 从暂存区中删除文件，且文件不会有未追踪的情况
git rm test.txt
git rm -f test.txt
```

### 1.14移动(mv)

- 相当于三条命令的结合
- mv .., git rm .., git add ..

```sh
git mv file1 file2  # 将file1重命名为file2
```

### 1.15查看更新(diff)

```sh
git diff  # 查看暂未暂存的文件更新哪些部分

# 查看暂存起来(即add之后)的更新
git diff --cached
git diff --staged

git diff --check  # 检查空白错误，可以在提交之前运行一次
git diff HEAD  # 检查自上次提交以来的所有变化
git diff <branch>  # 查看和某个分支的不同
git diff --diff-filter=MRC  # 仅仅查看修改，重命名等，不看增删
```

### 1.16远程(remote)

- 对远程仓库的操作
- origin也并没有特殊含义

```sh
# 查看配置的远程仓库服务器,如果是clone的则默认为origin
git remote
git remote -v  # 读写仓库服务器以及对应的简写url

git remote add tom https://github.com/tom/liu_aistuff  # 添加远程仓库，并设置简写,那么本地fetch之后就可以在tom/master访问
git remote show origin  # 查看某个远程仓库的更多信息
git remote rename tom tom1  # 将远程分支重命名
git remote remove tom  # 移除远程仓库(适用于远程仓库搬走了或者没人贡献了场景)

git ls-remote origin  # 查看远程分支列表
```

### 1.17清除(clean)

```sh
git clean -n  # 演示，查看哪些文件会被删除
git clean -f  # 删除当前目录下所有没有track的文件,不清理.gitignore文件中指定的文件和文件夹
git clean -df  # 删除当前目录下所有没有没有被track的文件和文件夹
git clean -xf  # 删除当前目录下的所有文件和文件夹，不管是否在.gitignore中指定
```

## 2.操作命令组

### 2.1修改已经push的commit的message

- [已经push的commit如何修改message](https://www.jianshu.com/p/ec45ce13289f)

```sh
# 1.确定修改哪些commit
git rebase -i HEAD~5

# 2.在vim中将待修改的commit的 pick 改为 edit，然后保存退出，此时git的分支发生改变，改成了我们第一个edit的commit id
# 3.在当前分支轮流执行（有几条message要修改就执行几次）以下两个命令,执行完第一个命令，修改message保存
git commit --amend
git rebase --continue
```

### 2.2修改多次commit的信息为一个

```sh
# 1.定位到指定的commit，修改commit的message，倒数的修改为`squash`
git rebase -i <commit_id>

# 2.修改掉多余的commit message
git rebase --continue
```

### 2.3提交之后因为大文件而push失败

```sh
# 1.回退至指定的版本号
git reset --hard `commit_id`

# 2.远程提交回退

git push origin HEAD --force

# 3.删除缓存
git rm -r --cached .
```

### 2.4提交错误且已经push到远程

```sh
# 1.本地撤销到指定版本
git reset --soft <commit_id>

# 2.取消对所有文件的头指针指向
git reset --HEAD ./

# 3.重新提交xxx

# 4.重新推送到远程,必须要-f
git push -f
```

## 3.gitignore文件

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

## 4.gitmodule

### 4.1介绍

- gitsubmodule是多项目使用共同类库的工具。

### 4.2使用

```sh
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

```sh
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

## 5.其他

### 5.1非常用命令

```sh
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

```sh
rm -rf .git/index
git reset --mixed HEAD
```

**错误的commit并提交到远程:**

```sh
git log
git reset --soft HEAD~2  # 不删除工作空间改动代码，撤销commit，不撤销git add . 或者将HEAD~2改为回退到的版本号
git push origin 分支名 --force  # 将当前撤销的提交推送到远程
```

### 5.2github

#### 5.2.1github搜索技巧

```sh
# 名字包含python，stars数量大于1000
python in:name stars:>1000

in:readme

in:description

language:python

pushed:2020-01-01
```

#### 5.2.2github知识

fork的作用：

当想参与某个项目，但是没有推动权限的时候，将其fork一个副本到自己的仓库，在本地修改之后可以通过创建`拉取请求(pull request, pr)`,将改动进入原项目仓库。

### 5.3在服务器上搭建git

```sh
# 1.将当前仓库导出为裸仓库-不包含当前目录的仓库
git clone --bare my_project my_project.git

# 2.将本地裸仓库放到服务器上,加入是放入/srv/git目录下
scp -r my_project.git user@git.example.com:/srv/git

# 3.如果一个用户对该目录/srv/git目录有读写权限，即可推送了
```

### 5.4如何选择git的分支模式

- [如何选择git分支模式](https://mp.weixin.qq.com/s/9Ey04P5Xv4W95N2FEioZ1g)

#### 5.4.1TBD

- `主干开发模式`
- 在一个分支开发，变更要小，要快速完成验证
- 适合`小规模`团队

#### 5.4.2Git-Flow模式

- `feature(新功能分支)`，开发者从develop分支拉取新的分支，开发完成，再merge到develop分支
- `develop(新功能集成分支)`，永远是保存开发集成中最新的版本，代码验证可发布之后，单独从develop分支拉release分支进行发布
- `release(版本发布分支)`，如果有缺陷修改，会同步到develop和master分支
- `hotfix(线上缺陷紧急修改分支)`，从master拉出，修复后验证，并将问题修复合并到develop和release上
- `master(保存最新发布版本基线的分支`)，主干分支，保存的是可工作版本的基线,即稳定随时可以上线的分支
- 适合`大规模团队`

#### 5.4.3Github-Flow模式

- master分支永远是所有代码最新可部署，可工作的版本
- 新工作从master拉取新分支
- 尽可能频繁的同步服务端同名的分支
- 合并到master，直接发起 `pull request`，请代码评审，评审通过，合并到master

#### 5.4.4Gitlab-Flow模式

- 类似于github-flow模式，开发将`pull request` 改成了 `merge request`

### 5.5git-lfs使用

#### 5.5.1概述

- [简书: git-lfs使用](https://www.jianshu.com/p/493b81544f80)
- github开发的git扩展，用于实现git对大文件的支持, 可以减少提交的变动量
- 在检出版本时,根据指针的变化情况下更新对应的大文件.而不是在本地保存所有版本的大文件

#### 5.5.2使用

```sh
# 1.mac安装
brew install git-lfs
git lfs install  # 开启git-lfs功能


# 2.文件追踪
git lfs track  # 查看当前的文件追踪模式
git lfs track "*.mp4"  # 追踪所有的.mp4文件


# 3.提交代码需要将gitattributes文件提交至仓库. 它保存了文件的追踪记录

# 4.可以查看当前跟踪的文件列表
git lfs ls-files

# 5.将代码 push 到远程仓库后
git add *.mp4
git commit
git push

# LFS 跟踪的文件会以『Git LFS』的形式显示:
# clone 时 使用'git clone' 或 git lfs clone均可
```

