from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
# Create your models here.
