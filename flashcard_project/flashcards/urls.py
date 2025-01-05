from django.urls import path
from .views import UserListView, CategoryListView, CardListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('cards/', CardListView.as_view(), name='card-list')
]