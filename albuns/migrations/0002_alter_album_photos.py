# Generated by Django 4.2.1 on 2023-06-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
        ('albuns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(blank=True, to='photos.photo', verbose_name='Fotos'),
        ),
    ]
