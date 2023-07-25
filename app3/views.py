from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def str1(request):
    return HttpResponse ("<center><h1>This is for third app string response</h1></center>")

def new5(request):
    return render (request,'new5.html')

def new6(request):
    return render (request,'new6.html')