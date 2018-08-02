from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title 

    def summary(self):
        return self.body[:1000]  # dame los primeros 1000 lineas

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')  # para poner la fecha como quiero
