from django.db import models

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'user'


class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    userId = models.ForeignKey('user', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'category'  

class Card(models.Model):
    id = models.BigIntegerField(primary_key=True)
    front = models.TextField()
    back = models.TextField()
    categoryId = models.ForeignKey('Category', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'Card'  
