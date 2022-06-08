from datetime import datetime
from statistics import mode
from django.db import models
from django.forms import CharField
import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateTimeField(default=datetime.datetime.now)
