from django.urls import path
from .           import views   

urlpatterns = [
     path('', views.index, name='index'),
     path('owner', views.owner, name='owner'),
     path('<int:question_id>/', views.details, name='details'),
     path('vote/<int:question_id>', views.vote, name='vote'),
     path('results/<int:question_id>', views.results, name='results'),

#    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
]