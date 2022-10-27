from django.db import models

# Create your models here.

class Article(models.Model):
    goods_url = models.TextField()
    goods_img_url = models.TextField()
    goods_category = models.TextField()
    goods_brand = models.TextField()

