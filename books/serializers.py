from rest_framework import serializers
from books.models import Book

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)
        
        
class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title','author','code')