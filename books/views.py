from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView, ListCreateAPIView , RetrieveUpdateDestroyAPIView
from books.models import Book
from books.serializers import BookListSerializer , BookDetailSerializer

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    
class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    