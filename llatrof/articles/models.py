from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.TextField(unique=True)

class Brand(models.Model):
    brand = models.TextField(unique=True)

class Article(models.Model):
    goods_url = models.TextField()
    goods_img_url = models.TextField()
    goods_category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        db_column='goods_category',
        to_field='category',
    )
    goods_brand = models.ForeignKey(
        Brand, 
        on_delete=models.CASCADE,
        db_column='goods_brand',
        to_field='brand',
    )
