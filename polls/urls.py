# 调用view视图，需要映射url

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]