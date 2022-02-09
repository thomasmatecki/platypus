"""
"""
from django.db import models


class Space(models.Model):
    """
    For rent.
    """

    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
