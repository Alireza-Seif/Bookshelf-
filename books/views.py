from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView 
from rest_framework.permissions import IsAuthenticated ,  IsAuthenticatedOrReadOnly
from books.models import Book
from books.serializers import BookListSerializer , BookDetailSerializer

class BookList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    
class BookDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    