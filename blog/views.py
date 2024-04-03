from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def article(request,num):
    if num in ['01','02','03']:
        return render(request,f"blog/article_{num}.html")
    return render(request,"blog/article_not_found.html")