from django.db import models
import random,string

def generate():
    while True:
        ret=random.choices(string.digits+string.ascii_letters, k=10)
        if Post.objects.filer(name=ret).count()==0:
            return ret

# Create your models here.
class Post (models.Model):
    name = models.CharField (primary_key=True, max_length=10, default=generate)
    content = models.TextField ()
