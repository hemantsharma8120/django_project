from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=30)
    discription=models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        db_table='category'


class Product(models.Model):
    title=models.CharField(max_length=20)
    discription=models.TextField()
    image=models.ImageField(upload_to='images')
    add_date=models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table='product'