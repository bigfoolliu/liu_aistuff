# java技巧

<!-- vim-markdown-toc Marked -->

* [1.pyenv进行java版本管理](#1.pyenv进行java版本管理)

<!-- vim-markdown-toc -->

## 1.pyenv进行java版本管理

- [jenv使用](https://www.dazhuanlan.com/2020/02/13/5e44f73763565/)
- [jenv官网](https://www.jenv.be/)

```sh
# 查看java安装版本和路径
/usr/libexec/java_home -V

brew install jenv

# 添加java版本
jenv add /Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk/Contents/Home

# 列出所有版本
jenv versions

# 切换版本，如下切换为1.7
jenv global 1.7

# 切换当前目录下的jdk版本，如切换当前目录下的版本为1.6
jenv local 1.6

# 查看当前jdk的信息
jenv info java

# 激活导出JAVA_HOME
jenv enable-plugin export

# 显示所有的插件
jenv plugins

# 启动一个版本的shell
jenv shell 1.6

# 配置maven中的java版本切换
jenv enable-plugin maven

```

