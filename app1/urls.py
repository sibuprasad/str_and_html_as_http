app_name='new'

from django.urls import path
from app1.views import *

urlpatterns = [
    path('str1/',str1,name='str1'),
    path('new1/',new1,name='new1'),
    path('new2/',new2,name='new2'),
]
