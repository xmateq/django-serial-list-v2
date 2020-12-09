from actors_list.utils import call_api
from django.db import models
import datetime
from django.core.validators import MinValueValidator

class Serial(models.Model):
    title = models.CharField(max_length=200)
    number_of_seasons = models.IntegerField(default=0)
    release_year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1800)])
    api_title = models.CharField(max_length=200, default=0)
    slug = models.CharField(max_length=200, default=0)
    imdb = models.CharField(max_length=100, default=0)

    def save(self, *args, **kwargs):
        title = self.title
        api_data = call_api(serial_title=title)
        self.api_title = api_data['apititle']
        self.slug = api_data['slug']
        self.imdb = api_data['imdb']
        self.release_year = api_data['year']
        return super(Serial, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['title', 'release_year']


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

