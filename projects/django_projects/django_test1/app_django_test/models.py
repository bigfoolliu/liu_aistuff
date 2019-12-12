from django.db import models

# Create your models here.
# 创建第一个模型
"""
一个基本的 书籍/作者/出版商 数据库
	- 一个作者有姓，有名及email地址。
	- 出版商有名称，地址，所在城市、省，国家，网站。
	- 书籍有书名和出版日期。 它有一个或多个作者, 只有一个出版商
"""


class Publisher(models.Model):
	"""
	出版商模型,等同于下面这张表:
		CREATE TABLE "books_publisher" (
			"id" serial NOT NULL PRIMARY KEY,
			"name" varchar(30) NOT NULL,
			"address" varchar(50) NOT NULL,
			"city" varchar(60) NOT NULL,
			"state_province" varchar(30) NOT NULL,
			"country" varchar(50) NOT NULL,
			"website" varchar(200) NOT NULL
			);
	"""
	name = models.CharField(max_length=30)  # 出版商名称
	address = models.CharField(max_length=50)  # 地址
	city = models.CharField(max_length=60)  # 城市
	state_province = models.CharField(max_length=30)  # 所属省份
	country = models.CharField(max_length=50)  # 所属国家
	website = models.URLField()  # 出版商网站


class Author(models.Model):
	"""
	作者类
	"""
	first_name = models.CharField(max_length=30)  # 作者名
	last_name = models.CharField(max_length=40)  # 作者姓
	email = models.EmailField()  # 作者email


class Book(models.Model):
	"""
	书籍类
	"""
	title = models.CharField(max_length=30)  # 书籍标题
	authors = models.ManyToManyField(Author)  # 书籍的作者们,多对多
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # 书籍的出版商,删除出版商类实例时会删除所有书籍的出版商
	publication_date = models.DateField()  # 出版日期
