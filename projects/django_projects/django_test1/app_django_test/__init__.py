# 更改数据库为MySQL需要在应用文件的初始化文件中添加
import pymysql
pymysql.install_as_MySQLdb()
