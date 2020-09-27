# java

<!-- vim-markdown-toc Marked -->

* [1.基础](#1.基础)

<!-- vim-markdown-toc -->

## 1.基础

### 1.1安装使用

- [mac配置java环境](https://www.zhihu.com/question/29114464)
- [jre与jdk的区别](https://blog.csdn.net/zhongguomao/article/details/91347743)
- jdk包含jre, jre包含jvm

```sh
# 查看版本
java --version

# 单文件编译
javac xxx.java

# 运行编译后的文件
java xxx.class
```

### 1.2基础语法

- `大小写敏感`：Java 是大小写敏感的，这就意味着标识符 Hello 与 hello 是不同的
- 类名：对于所有的类来说，`类名的首字母应该大写`。`如果类名由若干单词组成，那么每个单词的首字母应该大写`，例如 MyFirstJavaClass
- 方法名：所有的`方法名都应该以小写字母开头`。如果方法名含有若干单词，则后面的每个单词首字母大写
- 源文件名：`源文件名必须和类名相同`。当保存文件的时候，你应该使用类名作为文件名保存（切记 Java 是大小写敏感的），文件名的后缀为 .java。（如果文件名和类名不相同则会导致编译错误）
- 主方法入口：`所有的 Java 程序由 public static void main(String[] args) 方法开始执行`

源文件：

- 一个源文件中只能有一个 public 类
- 一个源文件可以有多个非 public 类
- 源文件的名称应该和 public 类的类名保持一致
- 如果一个类定义在某个包中，那么 package 语句应该在源文件的首行
- 如果源文件包含 import 语句，那么应该放在 package 语句和类定义之间。如果没有 package 语句，那么 import 语句应该在源文件中最前面
- import 语句和 package 语句对源文件中定义的所有类都有效
