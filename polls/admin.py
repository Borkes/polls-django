from django.contrib import admin

# Register your models here.
from .models import Question
admin.site.register(Question)  # 我们得告诉管理页面，问题 Question 对象需要被管理