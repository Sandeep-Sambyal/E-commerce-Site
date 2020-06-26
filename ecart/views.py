from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil
# Create your views here.

def index(request):
    allProds = []
    val = Products.objects.values('category', 'id')
    val2 = {item['category'] for item in val}
    str1 = ""
    for val2 in val2:
        prod = Products.objects.filter(category=val2)
        val = [item.product_name for item in prod]
        for a in val:
            print(a)
        str1 = str1 + ","
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        """str1=str1+str(prod)
        a=[item['product_name']  in prod]
            print(item)"""
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'ecart/index.html', params)




def about(request):
    return HttpResponse("ABOUT US PAGE")

def contact(request):


    allProds = []
    val = Products.objects.values('category', 'id')
    val2 = {item['category'] for item in val}
    str1=""
    for val2 in val2:
        prod = Products.objects.filter(category=val2)
        val=[item.product_name for item in prod]
        for a in val:
            print(a)
        str1=str1+","
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        """str1=str1+str(prod)
        a=[item['product_name']  in prod]
            print(item)"""
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
        #for a in allProds:
    #print(params)
    return render(request,'ecart/contact.html',params)

def orders(request):
    return HttpResponse("ORDERS PAGE")
def search(request):
    return HttpResponse("SEARCH PAGE")
def checkout(request):
    return HttpResponse("checkout PAGE")
def products(request , myid):
    product = Products.objects.filter( id = myid)
    print(product)
    return render(request,'ecart/products.html',{'Product':product[0]})

def seller(request):
    return render(request,'ecart/SellerForm.html')