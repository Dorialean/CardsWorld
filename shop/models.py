from django.db import models
from face.models import Person
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField()
    size = models.CharField(max_length=6)
    company_name = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    weight = models.CharField(max_length=10)

class Order(models.Model):
    person_id = models.ForeignKey(Person,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
