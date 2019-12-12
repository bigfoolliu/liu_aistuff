from django.contrib import admin

# 导入模型
from .models import *

# Register your models here.
# 无法看到应用，必须先在admin中进行注册，告诉admin站点，将模型加入站点内，接受站点的管理。

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
