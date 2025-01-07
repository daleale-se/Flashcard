from django.db import models

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField()
    email = models.EmailField()
    password = models.CharField()

    class Meta:
        managed = False
        db_table = 'User'


class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField()
    userId = models.ForeignKey('User', on_delete=models.CASCADE, db_column='userId')

    class Meta:
        managed = False
        db_table = 'Category'  


class Card(models.Model):
    id = models.BigIntegerField(primary_key=True)
    front = models.CharField()
    back = models.CharField()
    categoryId = models.ForeignKey('Category', on_delete=models.CASCADE, db_column='categoryId')
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'Card'  
