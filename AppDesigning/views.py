from django.http import HttpResponse
from django.shortcuts import render

def launch(request):
    #return render(request,'index.html')
    return render (request, 'index.html')