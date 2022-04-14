


from django.shortcuts import render
from django.http import HttpResponse

def fun(request):
    return HttpResponse('hello world')

def fun1(request):
    return HttpResponse('hai')

def fun2(request):
    return render(request, 'a.html')
