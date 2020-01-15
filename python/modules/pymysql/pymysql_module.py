"""
1. 首先需要安装好MySQL数据库并能正常运行

2. 连接数据库
当前的MySQL运行在本地，用户名为tonyliu，密码为123456，运行端口为3306。
这里利用PyMySQL先连接MySQL，然后创建一个新的数据库，名字叫作spiders。
"""
import pymysql

# 通过connect()方法声明一个MySQL对象data_base，需要传入运行的host(即IP)
# 本地运行，传入localhost，远程运行的则传入公网IP地址
data_base = pymysql.connect(host='localhost', user='tonyliu', password='123456', port=3306)

# cursor()方法获得MySQL的操作光标，用游标来执行sql语句，execute()方法即执行
cursor = data_base.cursor()
cursor.execute('SELECT VERSION()')  # 获得当前MySQL版本

# fetchone()方法获得第一条数据，得到上述版本号
data = cursor.fetchone()
print('Database version:', data)

# 直接创建默认编码为utf-8的数据库spiders
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
data_base.close()


"""
3. 创建表

此操作在之前创建的spiders数据库上执行
"""
# import pymysql
# # 建立连接
# db = pymysql.connect(host='localhost', user='tonyliu', password='123456', port=3306, db='spiders')
# # 获得操作光标
# cursor = db.cursor()
# # sql语句，在spiders数据库下创建了一个名为students的数据表，数据表下包含
# # id，name，age三个简单字段
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) not NULL, age INT NOT NULL, PRIMARY KEY (id))'
# # 执行上述sql语句
# cursor.execute(sql)
# # 关闭mysql对象
# db.close()


"""
4. 向表中插入数据

涉及事务问题，事务机制可以确保数据的一致性，即不存在数据插入一半的情况。事务四个属性如下：
也被称为事务的ACID特性：
属性      解释
原子性    事务是不可分割的工作单位，事务中包括的操作要么都做，要么都不做
一致性    事务必须是数据库从一个一致性状态变为另一个一致性状态
隔离性    一个事务的执行不能被其他事务干扰，即并发执行的事务之间不能互相干扰
持久性    一个事务一旦提交，对数据库中的改变时永久性的，接下来的其他操作或故障对其没有影响


数据插入，更新，删除操作都是对数据库进行更改的操作，标准写法是：
"""
# import pymysql
#
# # 假使爬取数据如下
# id = '201303164006'
# name = 'Tony'
# age = 20
#
# # 建立mysql连接
# db = pymysql.connect(host='localhost', user='tonyliu', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
#
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, name, age))
#     # commit()方法实现数据的插入，是真正将语句提交到数据库执行的方法
#     db.commit()
# except:
#     # 异常时，调用rollback()方法，实现数据回滚，即什么都没有发生过
#     db.rollback()
# db.close()


"""
另一种便于改动数据的插入方法
"""
# import pymysql
#
# db = pymysql.connect(host='localhost', user='tonyliu', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
#
# # 传入的数据为字典
# data = {
#     'id':'201403164006',
#     'name':'Jane',
#     'age':20
# }
#
# table = 'students'# 表名
# keys = ', '.join(data.keys())# 字典的keys()，keys结果为id, name, age
# values = ', '.join(['%s'] * len(data))# 几个参数就需要几个占位符%s
#
# # 下方语句含义可参照上一段语句，等价于：sql = INSERT INTO students(id, name, age) VALUES (%s, %s, %s)
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
#
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('successed.')
#         db.commit()
# except:
#     print('failed.')
#     db.rollback()
#
# db.close()


"""
5. 更新数据

最简单的方式仍然是构造一个sql语句然后执行
"""
# import pymysql
#
# db = pymysql.connect(host='localhost', user='tonyliu', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
#
# # 数据库students中的name = %s 的age改为%s
# sql = 'UPDATE students SET age = %s WHERE name = %s'
#
# try:
#     cursor.execute(sql, (19, 'Tony'))
#     db.commit()
# except:
#     db.rollback()
# db.close()


"""
实际抓取的过程中，更新数据实际上是希望不会出现重复数据，如果出现，应该是将数据更新只保存一遍
"""
# import pymysql
#
# db = pymysql.connect(host='localhost', user='tonyliu', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
#
# # 需要更新的数据
# data = {
#     'id':'201403164006',
#     'name':'Jane',
#     'age':21
# }
#
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
#
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
#
# update = ','.join(["{key} = %s".format(key=key) for key in data])
#
# sql += update
#
# try:
#     if cursor.execute(sql, tuple(data.values())*2):
#         print('successed.')
#         db.commit()
# except:
#     print('Failed.')
#     db.rollback()
# db.close()


"""
6. 删除数据

删除条件有多种多样，运算符有大于、小于、等于、LIKE等，条件连接符有AND、OR等
"""
# import pymysql
#
# db = pymysql.connect(host='localhost', user='tonyliu', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
#
# table = 'students'
# condition = 'age = 20'
#
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()


"""
7. 查询数据
"""
# import pymysql
#
# db = pymysql.connect(host='localhost', user='tonyliu', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
#
# sql = 'SELECT * FROM students WHERE age = 19'
#
# """
# try:
#     cursor.execute(sql)
#     print('count:', cursor.rowcount)
#
#     # fetchone()获得结果的第一条数据
#     # one = cursor.fetchone()
#     # print('one:', one)
#
#     # fetchall()方法可以获得结果的所有数据，但如果数据量大的话，将会大量占用内存
#     results = cursor.fetchall()
#     print('results:', results)
#     print('results type:', type(results))
#
#     # 此处的results为二重元组，因此将每个元素遍历出来
#     for row in results:
#         print(row)
# except:
#     db.rollback()
# """
# # while + fetchone()方法获取所有数据
# try:
# 	cursor.execute(sql)
# 	row = cursor.fetchone()
# 	while row:
# 		print('row:', row)
# 		row = cursor.fetchone()
# except:
# 	print('error.')
# 	db.rollback()
#
# db.close()
