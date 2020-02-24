# git相关知识

## 1.git基本命令

### 1.1版本和用户

```shell
# 一般配置
# 查看版本信息
git --version

# 获取当前登陆的用户
git config --global user.name

# 获取当前登陆用户的邮箱
git config --global user.email

# 直接进入编辑全局配置文件
git config -e --global

# 登陆git
# 设置全局git账户，userName为用户名
git config --global user.name "userName"
git config --global user.email "userEmail"

# 设置单个仓库的git账户
git config user.name "userName"
git conig user.email "userEmail"

# 查看当前git配置
git config --list

# 将git的文本编辑器修改为vim
git config --global core.editor vim
```

### 1.2仓库克隆

```shell
# 从远程克隆一个版本库
git clone `address`
```

### 1.3暂存

```shell
# 将所有修改文件暂存
git add .

# 将指定文件暂存
git add test.py

# reset撤销直接删除指定的commit,将HEAD后移
# 撤销对所有文件的暂存
git reset HEAD

# 撤销对指定文件的暂存
git reset HEAD test.py
```

### 1.4本地提交

```shell
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
```

### 1.5远程提交与拉取

```shell
# 当前分支只有一个追踪分支，直接将本地的分支的更新推送至远程主机
git push
git push <远程主机名>　<本地分支名>:<远程分支名>

# 当前分支只有一个追踪分支，直接取回远程主机某个分支的更新，与本地的分支合并
git pull
# 与本地的指定合并
git pull <远程主机名>　<远程分支名>:<本地分支名>

# 强制推到远程(慎用)
git push -f
```

### 1.6提交堆栈

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
# 将当前stash中的内容应用到当前分支对应的工作目录（不会删除堆栈中最近保存的内容）
git stash apply
# 删除所有存储的进度
git stash clear
```

### 1.7分支

```shell
# 取回所有分支的更新
git fetch
# 取回指定的分支更新(eg:git fetch origin master)
git fetch <远程主机名> <分支名>

# 切换到本地的dev分支
git checkout `dev`
# 建立一个新的本地dev分支
git checkout -b `dev`

# 当文件提交comnit后push因为大文件而失败
# 回退至指定的版本号
git reset --hard `commit_id`
# 远程提交回退
git push origin HEAD --force
# 删除缓存
git rm -r --cached .


# 查询本地仓库，远程仓库，跟踪关系最全的命令
git branch -vv -a

# 获取远程仓库的地址
git remote get-url origin
```

### 1.8撤销

```shell
# revert会将操作之前和之后的信息都会保留,用新的commit回滚旧的commit
# 撤销前一次commit
git revert HEAD

# 撤销前前一次commit
git revert HEAD^

# 撤销指定的版本
git revert commit d92761fec08ecca646f81402a415e9a07f9638b6
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

## a.其他

```shell
# 查看当前状态
git status

# 查看commit的日志
git log

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

