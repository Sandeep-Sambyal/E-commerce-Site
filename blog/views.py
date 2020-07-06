from django.http import HttpResponse

from django.shortcuts import render
from .models import blogpost

# Create your views here.

def index(request):
    obj=blogpost.objects.all()
    print(obj)
    param={'data':obj}

    return render(request,'blog/index.html',param)

def blogposted(request,id):
    post=blogpost.objects.filter(blog_id=id)[0]
    print(post)
    return render (request,'blog/blogpost.html',{'data':post})
