# Generated by Django 4.1.3 on 2022-11-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Fruit slug'),
        ),
    ]