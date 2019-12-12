from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)  # 问题文本
	pub_date = models.DateTimeField('date published')  # 发布日期

	def was_published_recently(self):
		"""判断是够最近发布到的"""
		now = timezone.now()
		# return self.pub_date >= timezone.now() - timedelta(days=1)
		return now - timedelta(days=1) <= self.pub_date <= now
	# 修改样式
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently'

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	# 外键的定义需要写在"多"的一方
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text


