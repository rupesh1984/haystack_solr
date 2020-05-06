from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


from django.core.validators import MaxValueValidator, MinValueValidator

class Catalog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)



