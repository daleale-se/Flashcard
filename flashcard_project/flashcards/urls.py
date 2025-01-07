from django.urls import path
from .views import UserListView, CategoryListView, CardListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('cards/', CardListView.as_view(), name='card-list')
]