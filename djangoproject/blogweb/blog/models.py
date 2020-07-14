from django.db import models
from datetime import datetime
from users.models import Adduser
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(to=Adduser,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=2000)
    category = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.author}"