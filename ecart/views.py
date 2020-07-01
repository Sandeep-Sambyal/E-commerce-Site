from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,CustomerData
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
        str1 = str1 + ","
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
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
    return render(request,'ecart/order.html')
def search(request):
    return HttpResponse("SEARCH PAGE")
def checkout(request):
    return render(request,'ecart/order.html')

def products(request , myid):
    product = Products.objects.filter( id = myid)
    return render(request,'ecart/products.html',{'Product':product[0]})

def seller(request):
    if request.method=="POST":
        fname =request.POST.get('Firstname','')
        lname =request.POST.get('lastname','')
        email =request.POST.get('email','')
        address =request.POST.get('Address','')
        name =request.POST.get('Firstname','')
        state=request.POST.get('State','')
        zip=request.POST.get('zip','')
        country=request.POST.get('country','')
        same_addr=request.POST.get('same_addr','false')
        phone=request.POST.get('phone','')

        name=fname.strip() + " " + lname.strip()
        address=address.strip()+" "+state.strip()+" "+zip+" "+country


        if same_addr=='false':
            custdata=CustomerData(seller_profile="R",CustomerName=name,email=email,seller_address =address ,phone=phone,country=country)
            custdata.save()
        else:
            custdata = CustomerData(seller_profile="R", CustomerName=name, email=email, seller_address=address, shipping_address=address,phone=phone,country=country )
            custdata.save()

    param={'countrylist':['India','Nepal','Pakistan','Sri Lanka','Bangladesh']}
    return render(request,'ecart/SellerForm.html',param)