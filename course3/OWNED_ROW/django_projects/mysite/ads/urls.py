from django.urls import reverse_lazy
from django.urls import path 
from  . import views

app_name = "ads"

urlpatterns = [
    path('',views.AdListView.as_view()), 
    path('ads',views.AdListView.as_view(),name='all'),    
    path('ad/<int:pk>',views.AdDetailView.as_view(),name="ad_detail"),
    ## you can actually set a success reverse in  here too
    path('ad/create',views.AdCreateView.as_view(success_url = reverse_lazy('ads:all')),name="ad_create"),
    path('ad/<int:pk>/update',views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')),name="ad_update"),
    path('ad/<int:pk>/delete',views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')),name='ad_delete'),
]
