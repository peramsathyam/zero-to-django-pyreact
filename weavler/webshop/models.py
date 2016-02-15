from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.


@python_2_unicode_compatible  # python 2 support for unicode
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
