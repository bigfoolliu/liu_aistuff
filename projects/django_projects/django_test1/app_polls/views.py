from django.shortcuts import render, get_object_or_404
# 导入响应模块
from django.http import HttpResponse, Http404, HttpResponseRedirect
# 导入模型
from .models import *
# 为了使用模板,需要导入
# from django.template import loader

from django.urls import reverse

# 为了类视图的需要导入
from django.views import generic


# Create your views here.
# def index(request):
# 	"""第一个视图"""
# 	# # 将最近的5个问题按照倒序输出
# 	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# # 注意是将文本交给浏览器解析换行要根据html的规则
# 	# output = '<br>'.join([q.question_text for q in latest_question_list])
# 	# # print(output)
# 	# return HttpResponse(output)
#
# 	# 上面属于硬编码,下方为利用模板
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# 指定使用的模板
# 	# template = loader.get_template('app_polls/index.html')
# 	# 指定模板中需要替换的内容
# 	context = {
# 		'latest_question_list': latest_question_list,
# 	}
# 	# return HttpResponse(template.render(context, request))
# 	# 加载模板,传递参数,返回HttpResponse对象非常常用,使用render函数直接替换上句以及template定义语句
# 	return render(request, 'app_polls/index.html', context)
#
#
# def detail(request, question_id):
# 	"""问卷的具体内容"""
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist.")
# 	# return HttpResponse("You're looking at question %s." % question_id)
# 	# 新写法
# 	context = {'question': question}
# 	return render(request, 'app_polls/detail.html', context)
#
#
# def results(request, question_id):
# 	"""问卷的结果显示页面"""
# 	# response = "You're looking at the results of question %s."
# 	# return HttpResponse(response % question_id)
#
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'app_polls/results.html', {'question': question})


# 将上面的视图函数全部更改为类视图
class IndexView(generic.ListView):
	"""index.html的类视图
	继承类视图ListView,表示显示一个对象的列表"""
	template_name = 'app_polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""返回最近发布的5个问卷"""
		return Question.objects.order_by('-pub_date')[:5]


# DetailView类视图需要从url中捕获称为pk的主键值,因此将url中的<question_id>修改成了<pk>
class DetailView(generic.DetailView):
	"""detail.html的类视图
	继承DetailView表示显示特定类型对象得详细页面"""
	model = Question
	template_name = 'app_polls/detail.html'


class ResultsView(generic.DetailView):
	"""results.html的类视图"""
	model = Question
	template_name = 'app_polls/results.html'


def vote(request, question_id):
	"""投票处理"""
	# 此句为try...except未找到对象产生404error语句的缩写
	question = get_object_or_404(Question, pk=question_id)
	try:
		# request.POST是一个类似字典的对象，允许你通过键名访问提交的数据.
		# request.POST[’choice’]返回被选择选项的ID，并且值的类型永远是string字符串.
		# 为防止因为post里没有choice键值产生KeyError异常,加None解决,即改为request.POST['choice', None]
		selected_choice = question.choice_set.get(pk=request.POST['choice'])

		print(type(selected_choice), selected_choice)  # models中定义的模型(类)
	except (KeyError, Choice.DoesNotExist):
		# 发生choice未找到的异常时,重新返回表单页面,并给出提示
		return render(request, 'app_polls/detail.html', {
			'question': question,
			'error_message': 'You did not select a choice.',
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# 成功处理数据后,自动跳转至结果页面,防止用户多次连续提交
		# 在选择计数器加一后，返回的是一个HttpResponseRedirect而不是先前我们常用的HttpResponse。
		# HttpResponseRedirect需要一个参数：重定向的URL,对于所有的web开发,最好都要保持这种方式
		return HttpResponseRedirect(reverse('app_polls:results', args=(question.id,)))
		# return HttpResponse("You're voting on question %s." % question_id)
