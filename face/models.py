from django.db import models

# Create your models here.

class Person(models.Model):
    nickname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='avatars/%Y/%m/%d/')
    reg_date = models.DateTimeField(auto_now_add=True)
    order_id = models.ForeignKey('shop.Order',on_delete=models.CASCADE, default='No order')
