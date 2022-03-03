from django.db import models
from face.models import Person
# Create your models here.

class Articles(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.TextField()