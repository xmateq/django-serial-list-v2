import datetime

from django.db import models
from django.core import validators

class Serial(models.Model):
    title = models.CharField(max_length=200)
    number_of_seasons = models.IntegerField(default=0)
    release_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['title', 'release_date']


class Actor(models.Model):
    name = models.CharField(max_length=128)
    serials = models.ManyToManyField(to=Serial)

    def __str__(self):
        return self.name


class Comment(models.Model):
    com = models.TextField(max_length=1000)
    rate = models.IntegerField(default=1)
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)

    def __str__(self):
        return self.com

