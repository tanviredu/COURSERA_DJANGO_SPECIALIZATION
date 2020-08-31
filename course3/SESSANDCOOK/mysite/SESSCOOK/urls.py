from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('cookiefun',views.cookie,name="cookie"),
    path('sessfun',views.sessfun,name="sessfun"),
    path('/owner',views.owner,name="owner"),
    #path('/hello',views.hello,name="hello"),
    
]
