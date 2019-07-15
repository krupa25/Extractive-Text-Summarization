from django.db import models

# Create your models here.
class Article(models.Model):
    article = models.TextField(max_length=50000)
    summary = models.CharField(max_length=1000)