from django.db import models


# Create your models here.
class Post (models.Model):
    name = models.CharField (primary_key=True, max_length=10)
    content = models.TextField ()
