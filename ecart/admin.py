from django.contrib import admin

# Register your models here.
from .models import  Products,CustomerData
admin.site.register(Products)

admin.site.register(CustomerData)


