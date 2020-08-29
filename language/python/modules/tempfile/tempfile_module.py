"""
tempfile模块创建临时文件和目录

- 介绍：https://blog.csdn.net/zhtysw/article/details/82778354
- https://www.cnblogs.com/franknihao/p/8796571.html
"""


from tempfile import TemporaryFile

temp = TemporaryFile()
print(temp)
print(temp.name)

'''
TemporaryFile类的构造方法，其返回的还是一个文件对象。但这个文件对象特殊的地方在于
1. 对应的文件没有文件名，对除了本程序之外的程序不可见
2. 在被关闭的同时被删除
所以上面的两句打印语句，输出分别是一个文件对象，以及一个<fdopen>（并不是文件名）
'''
# 向临时文件中写入内容
temp.write(b'hello\nworld')

# ...一些操作之后需要读取临时文件的内容了
temp.seek(0)     # 从头读取，和一般文件对象不同，seek方法的执行不能少
print(temp.read())

temp.close()    # 关闭文件的同时删除文件

