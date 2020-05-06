from django.db import models

# Create your models here.
from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=True)
    address_line1 = models.CharField(max_length=500)
    address_line2 = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.first_name)

    def get_fullname(self):
        return self.first_name + " " + self.last_name
