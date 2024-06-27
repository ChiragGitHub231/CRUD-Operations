from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    email=models.EmailField()
    contact=models.IntegerField()
    address=models.CharField(max_length=50,blank=False,null=False)
    gender=models.CharField(max_length=10,blank=False,null=False)

    def __str__(self):
        return self.name