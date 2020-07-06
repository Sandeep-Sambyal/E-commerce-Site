from django.contrib import  admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='bloghome'),
    path('blogposted<int:id>',views.blogposted, name='blogposted')
]