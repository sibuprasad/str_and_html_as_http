from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def str1(request):
    return HttpResponse ("<center><h1>This is for second app string response</h1></center>")

def new3(request):
    return render (request,'new3.html')

def new4(request):
    return render (request,'new4.html')