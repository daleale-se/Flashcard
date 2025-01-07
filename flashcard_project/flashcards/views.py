from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Category, Card
from .serializers import UserSerializer, CategorySerializer, CardSerializer

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CardListView(APIView):
    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

def home(request):
    return render(request, 'home.html')
