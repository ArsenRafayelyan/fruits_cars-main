from enum import unique
from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField('Fruit name', max_length=30)
    img = models.ImageField('Fruit image', upload_to='media')
    descripion = models.TextField('Fruit description')
    slug = models.SlugField('Fruit slug', unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fruit'
        verbose_name_plural = 'Fruits'


class Car(models.Model):
    name = models.CharField('Car name', max_length=30)
    img = models.ImageField('Car image', upload_to='media')
    about = models.TextField('Car about')
    slug = models.SlugField('Car slug', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'