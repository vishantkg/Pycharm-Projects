import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#this is a request handler,
#gives a response for some action

def say_hello(request):
    x = 1
    y = 3
    return render(request, 'hello.html',{'name':'Vishant'})

