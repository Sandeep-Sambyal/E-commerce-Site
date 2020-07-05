from django.contrib import admin

# Register your models here.
from .models import  Products,CustomerData,Order,orderdetail
admin.site.register(Products)

admin.site.register(CustomerData)
admin.site.register(Order)
admin.site.register(orderdetail)


