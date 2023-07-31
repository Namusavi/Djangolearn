from  django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField(default=1)
    country = models.CharField(max_length=40, blank=False, default="kenya")
    city = models.CharField(max_length=9, blank=False, default="nairobi")
    age = models.IntegerField()
    gender = models.CharField(max_length=30, blank=False, null=False)

def __str__(self):
    return self.name
