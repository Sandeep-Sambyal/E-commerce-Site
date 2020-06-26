from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='shoplaunch'),
    path('about/',views.about,name='AboutUS'),
    path('contact/',views.contact,name='ContactUS'),
    path('orders/',views.orders,name='orders'),
    path('search/',views.search,name='search'),
    path('checkout/',views.checkout,name='checkout'),
    path('products/<int:myid>',views.products,name='products'),
    path('beaseller/',views.seller,name='sellerform')


]