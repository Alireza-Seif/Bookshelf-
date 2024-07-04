from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.BookDetail.as_view()),
    path('',views.BookList.as_view()),
]
