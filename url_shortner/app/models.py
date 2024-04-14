from django.db import models

# Create your models here.


class UrlToken(models.Model):
    url = models.URLField()
    token = models.CharField(max_length=10, unique=True)
