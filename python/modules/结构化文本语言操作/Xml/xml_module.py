#!-*-coding:utf-8-*-
# !@Date: 2018/8/19 9:28
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
Xml 是最突出的处理这种转换的标记（markup）格式，它使用标签（tag）分隔数据，
Xml 通常用于数据传送和消息，它存在一些子格式，如RSS 和Atom.

如下面的示例文件menu.xml 所示：

<?xml version="1.0"?>
<menu>
    <breakfast hours="7-11">
        <item price="$6.00">breakfast burritos</item>
        <item price="$4.00">pancakes</item>
    </breakfast>
    <lunch hours="11-3">
        <item price="$5.00">hamburger</item>
    </lunch>
    <dinner hours="3-10">
        <item price="8.00">spaghetti</item>
    </dinner>
</menu>


Xml 的一些重要特性：
• 标签以一个< 字符开头，例如示例中的标签menu、breakfast、lunch、dinner 和item；
• 忽略空格；
• 通常一个开始标签（例如<menu>）跟一段其他的内容，然后是最后相匹配的结束标签，
例如</menu>；
• 标签之间是可以存在多级嵌套的，在本例中，标签item 是标签breakfast、lunch 和
dinner 的子标签，反过来，它们也是标签menu 的子标签；
• 可选属性（attribute）可以出现在开始标签里，例如price 是item 的一个属性；
• 标签中可以包含值（value），本例中每个item 都会有一个值，比如第二个breakfast item
的pancakes；
• 如果一个命名为thing 的标签没有内容或者子标签，它可以用一个在右尖括号的前面添
加斜杠的简单标签所表示，例如<thing/> 代替开始和结束都存在的标签<thing> 和</
thing>；
• 存放数据的位置可以是任意的——属性、值或者子标签。例如也可以把最后一个item
标签写作<item price ="$8.00" food ="spaghetti"/>。
"""

"""python中解析XML最简单的方法是使用ElementTree"""
import xml.etree.ElementTree as et

tree = et.ElementTree(file="./menu.xml")
root = tree.getroot()
print(root.tag)

for child in root:
    print("tag: ", child.tag, "attributes:", child.attrib)
    for grandchild in child:
        print("\ttag: ", grandchild.tag, "attributes:", grandchild.attrib)
