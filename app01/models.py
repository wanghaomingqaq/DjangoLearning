from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish_data = models.DateField(auto_now_add=True)

    publish = models.ForeignKey(to='Publish',on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')



class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(to='AuthorDetail',on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)