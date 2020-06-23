from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil
# Create your views here.

def index(request):
    products =Products.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    allprods=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={'allproducts':allprods}
    print (params)

    """allProds=[]
           val=Products.objects.values('category','id')
           val2={item['category'] for item in val}
           for val2 in val2:
               prod=Products.objects.filter(category=val2)
               n=len(prod)
               nSlides = n // 4 + ceil((n / 4) - (n // 4))
               allProds.append([prod,range(1,nSlides),nSlides])


           params={'allProds':allProds}
           """
    return render(request, 'ecart/index.html', params)




def about(request):
    return HttpResponse("ABOUT US PAGE")

def contact(request):
    return render(request,'ecart/contact.html')
def tracker(request):
    return HttpResponse("TRACKER PAGE")
def search(request):
    return HttpResponse("SEARCH PAGE")
def checkout(request):
    return HttpResponse("checkout PAGE")
def productview(request):
    return HttpResponse("productview PAGE")