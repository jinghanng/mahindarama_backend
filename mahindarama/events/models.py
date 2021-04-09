from django.db import models


class Sangha(models.Model):
    name = models.CharField(max_length=100)

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


class Event_Creator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=300)
    location = models.ManyToManyField(Location)
    image = models.URLField(default='', blank=True)
    categories = models.ManyToManyField(Category)
    sangha_name = models.ManyToManyField(Sangha)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    publish_date = models.DateField()
    publish_by = models.ForeignKey(Event_Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
