from django.contrib import admin

# Register your models here.

# 向admin注册模型
from . import models
admin.site.register(models.Users)
