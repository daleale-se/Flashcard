from django.contrib import admin
from flashcards.models import Card, Category, User

admin.site.register(Card)
admin.site.register(Category)
admin.site.register(User)