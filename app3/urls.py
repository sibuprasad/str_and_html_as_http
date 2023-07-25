app_name='app3'

from django.urls import path
from app3.views import *

urlpatterns = [
    path('str1/',str1,name='str1'),
    path('new5/',new5,name='new5'),
    path('new6/',new6,name='new6'),
]
