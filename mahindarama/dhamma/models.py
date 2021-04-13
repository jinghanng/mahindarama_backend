from django.db import models

# Create your models here.
from django.db import models


class Sangha(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MediaType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dhamma(models.Model):
    title = models.CharField(max_length=500)
    location = models.ManyToManyField(Location)
    image = models.URLField(default='', blank=True)
    categories = models.ManyToManyField(Category)
    sangha_name = models.ManyToManyField(Sangha)
    record_date = models.DateField(blank=True, null=True)
    media_type = models.ManyToManyField(MediaType)
    duration = models.DurationField(blank=True, null=True)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.title
