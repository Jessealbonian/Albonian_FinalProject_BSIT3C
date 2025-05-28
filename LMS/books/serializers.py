from rest_framework import serializers
from .models import Category, books

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'