app_name='app2'

from django.urls import path
from app2.views import *

urlpatterns = [
    path('str1/',str1,name='str1'),
    path('new3/',new3,name='new3'),
    path('new4/',new4,name='new4'),
]
