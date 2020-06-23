from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='bloglaunch'),
    path('about/',views.about,name='AboutUS'),
    path('contact/',views.contact,name='ContactUS'),
    path('tracker/',views.tracker,name='track'),
    path('search/',views.search,name='search'),
    path('checkout/',views.checkout,name='checkout'),
    path('productview/',views.productview,name='Prdctview')


]