from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    url = models.CharField(max_length=150, verbose_name='Url')
    content = models.TextField(verbose_name='Post')