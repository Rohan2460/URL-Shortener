from django.db import models


class UrlToken(models.Model):
    url = models.URLField()
    token = models.CharField(max_length=10, unique=True)
