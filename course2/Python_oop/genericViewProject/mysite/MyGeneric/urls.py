from django.urls import path
from .views import PublisherList,PublisherDetail,BookCreate,UpdateBook,DeleteBook

urlpatterns = [
    path('publishers/',PublisherList.as_view(),name='p'),
    path('publisher/<int:pk>',PublisherDetail.as_view()),
    path('book/create',BookCreate.as_view()),
    path('book/update/<int:pk>',UpdateBook.as_view()),
    path('book/delete/<int:pk>',DeleteBook.as_view()),
]