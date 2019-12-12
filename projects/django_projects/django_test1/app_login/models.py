from django.db import models

# Create your models here.


class Users(models.Model):
	"""用户模型"""
	gender = (
		('male', "男"),
		('female', "女"),
	)

	# 用户名最长为128字节,且该字段的数据不可重复
	name = models.CharField(max_length=128, unique=True)
	password = models.CharField(max_length=256)
	# email为特殊的email字段类型
	email = models.EmailField(unique=True)
	sex = models.CharField(max_length=32, choices=gender, default="男")
	# 用户创建时间
	c_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	# 模型的元数据,添加例如排序方式、数据库表名、人类可读的单数或者复数名等等
	class Meta:
		ordering = ["-c_time"]  # 按照创建时间的降序排列
		verbose_name = "用户"  # 单数名为用户
		verbose_name_plural = "用户"  # 复数名为用户
