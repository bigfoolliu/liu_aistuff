#!-*-coding:utf-8-*-
# !@Date: 2018/8/27 16:34
# !@Author: Liu Rui
# !@github: bigfoolliu


from pymysql import connect

# 1. 准备连接数据库
conn = connect(host="localhost", port=3306, database="stock_db", user="tonyliu", password="123456", charset="utf8")
# 2. 获得游标
cur = conn.cursor()
# 3. 执行语句
sql_str = "SELECT * FROM info;"
cur.execute(sql_str)

# 4. 获取所有的表格数据
sql_result1 = cur.fetchall()

print(type(sql_result1))  # 返回的是元组类型数据

for item in sql_result1:
	print(item)

sql_str = "select info.code, info.short, info.chg, info.turnover, info.price, info.highs, stock_db.focus.note_info from info INNER JOIN focus WHERE info.id = focus.info_id;"
cur.execute(sql_str)
sql_result2 = cur.fetchall()

print(type(sql_result2))  # 返回的是元组类型数据

for item in sql_result2:
	print(item)

cur.close()

conn.close()
