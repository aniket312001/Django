from django.db import models

# Create your models here.
class details(models.Model):
    my_id = models.AutoField
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    marks = models.IntegerField()