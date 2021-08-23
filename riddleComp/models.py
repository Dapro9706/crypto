from django.db import models
import random,string

def generate():
    a=string.digits+string.ascii_letters+string.digits+string.digits
    while True:
        ret=''.join(random.choices(a, k=10))
        if Post.objects.filter(name=ret).count()==0:
            return ret

# Create your models here.
class Post (models.Model):
    name = models.CharField (primary_key=True, max_length=10, default=generate)
    content = models.TextField ()
