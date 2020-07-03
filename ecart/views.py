from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,CustomerData,Order,orderdetail
from math import ceil
import json
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

    return render(request,'ecart/contact.html')

def orders(request):
    if (request.method == "POST"):
        email=request.POST.get('email','')
        oid=request.POST.get('orderid','')
        print(email,oid)

        try:
            check=Order.objects.filter(order_id=oid , email=email)
            print(check[0].prod_list)
            if (len(check)>0):
                query=orderdetail.objects.filter(order_id=oid)
                text=[]

                for item in query:
                    text.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([text,check[0].prod_list],default=str)
                    print(response)
                return HttpResponse(response)
            else:
                return HttpResponse('Data provided is Incorrect')

        except Exception as e:
            return HttpResponse('if ')
        
    return render(request,'ecart/order.html')

def search(request):
    return HttpResponse("SEARCH PAGE")

def checkout(request):
    if (request.method == "POST"):
        name=request.POST.get("name","")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        Address = request.POST.get("Address1", "")+" "+request.POST.get("Address2", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")
        city= request.POST.get("city", "")
        prod_list=request.POST.get("customerlist","")

        val=Order(name=name,email=email,phone=phone,address=Address,prod_list=prod_list,state=state,zip_code=zip_code,city=city)
        val.save()
        thank=True
        order=val.order_id
        update=orderdetail(order_id=order, update_desc="Your order has been placed.")
        update.save()
        return render(request,'ecart/checkout.html',{'thank':thank,'orderid':order})

    return render(request,'ecart/checkout.html')

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