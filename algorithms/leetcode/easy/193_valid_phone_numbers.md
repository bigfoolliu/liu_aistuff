```text
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890

给一个文本文件 file.txt，里面包含多个电话号码（一行一个），写一个单行的bash脚本来输出所有合法的电话号码。
你可以假设一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）
你也可以假设每行前后没有多余的空格字符。
```

```shell
grep "^\(([0-9]\{3\}) \|[0-9]\{3\}-\)[0-9]\{3\}-[0-9]\{4\}$" file.txt

# 注意""不要丢了，其中的空格，()是普通字符，" "不要丢了
# ^：表示行首，以...开始，这里表示以(xxx) 或者xxx-开始，注意空格
# ()：选择操作符，要么是([0-9]\{3\}) ，要么是[0-9]\{3\}-
# |：或者连接操作符，表示或者
# []：单字符占位，[0-9]表示一位数字
# {n}：匹配n位，[0-9]\{3\}匹配三位连续数字
# $：表示行尾，结束
```