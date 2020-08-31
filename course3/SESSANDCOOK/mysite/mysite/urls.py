from django.contrib import admin
from django.urls import path,include
from SESSCOOK.views import hello
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls',include('SESSCOOK.urls')),
    path('hello',hello,name="hello")
]
