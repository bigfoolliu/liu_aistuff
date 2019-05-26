一般配置:

git --version       查看版本信息
git config --global user.name       获取当前登陆的用户
git config --global user.email      获取当前登陆用户的邮箱


登陆git:

git config --global user.name '<userName>'      设置git账户，userName为用户名
git config --global user.email '<userEmail>'
git config --global core.editor vim     将git的文本编辑器修改为vim

git clone <address>     从远程克隆一个版本库

git status      查看当前状态

git commit      直接提交
git commit -m "<message>"       带注释的提交
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

git checkout <dev>      切换到本地的dev分支
git checkout -b <dev>       建立一个新的本地dev分支

git config -e --global      直接进步编辑全局配置文件

当文件提交comnit后push因为大文件而失败:
git reset <id>　　回退至指定的版本号
git rm -r --cached .　　删除缓存
