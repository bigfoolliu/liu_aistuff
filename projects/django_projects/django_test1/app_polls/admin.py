from django.contrib import admin

# Register your models here.
from .models import *


# class ChoiceInline(admin.StackedInline):
# 两种不同的选项选择方式
class ChoiceInline(admin.TabularInline):
	"""在创建Question的时候可以再直接添加三个选择"""
	model = Choice
	extra = 3


# 定制模型表单
class QuestionAdmin(admin.ModelAdmin):
	"""自定义Question模型的表单页面"""
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Data information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

	# 定制实例表单
	list_display = ('question_text', 'pub_date', 'was_published_recently')

	# 增加一个过滤面板
	list_filter = ['pub_date']

	# 增加一个搜索框,且数量可以有多个
	search_fields = ['question_text']


# 分别注册该两个模型
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
