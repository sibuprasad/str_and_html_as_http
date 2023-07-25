from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def str1(request):
    return HttpResponse ("<center><h1>This is for string response</h1></center>")

def new1(request):
    return render (request,'new1.html')

def new2(request):
    return render (request,'new2.html')