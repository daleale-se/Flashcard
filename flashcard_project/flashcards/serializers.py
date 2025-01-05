from rest_framework import serializers
from .models import User, Category, Card

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

class CategorySerializer(serializers.ModelSerializer):
    userId = UserSerializer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'userId']

class CardSerializer(serializers.ModelSerializer):
    categoryId = CategorySerializer()

    class Meta:
        model = Card
        fields = ['id', 'front', 'back', 'categoryId', 'createdAt']
