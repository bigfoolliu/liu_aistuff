# vi快捷键

x   删除光标出的字符
dd  delete the whole line
i   insert before the cursor
a   insert after the cursor
o   insert a new line at the current line
u   撤销最后一次更改

:q!  不保存退出
:wq     保存退出
:e!     放弃所有修改，从上次保存开始处再编辑
ZZ  保存并退出

vi `file`   open single file
vi `file1` `file2`  open multi file

:open `file`    在vi窗口中打开一个新文件
:split `file`   在新窗口中打开一个新文件

/text   查找text,按n键查找下一个,按Ｎ查找前一个

:`number`   跳转到指定的行

u   撤销上一步操作

dd  删除当前行
10d 删除当前开始的10行
Ｄ  删除当前字符至行尾

yy  拷贝当前行
2yy 拷贝当前后开始的2行
p   粘贴

:1, 10 copy 20  将1-10行的内容复制到20行
:1, 10 move 20  将1-10行的内容剪切到20行

:%s/A/B/g  将所有的A替换为B

g   快速跳转至文件开头
G   快速跳转至文件末尾
