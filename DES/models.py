from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to = 'DES/files')
    product_disc = models.IntegerField()
    product_category = models.CharField(max_length=100)
    def __str__(self) :
        return self.product_name
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    query = models.CharField(max_length=500)

    def _str_(self):
        return self.name


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = "default.jpg", upload_to = "DES/files")

    def __str__(self):
        return f'{self.user.username} Profile'
