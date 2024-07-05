from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class BookListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False)
    class Meta:
        model = Book
        fields = '__all__'
        
class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'