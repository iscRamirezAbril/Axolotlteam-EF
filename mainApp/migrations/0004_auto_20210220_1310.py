# Generated by Django 3.1.7 on 2021-02-20 21:10

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20210220_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubications',
            name='description',
            field=models.TextField(default='', verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='ubications',
            name='documentacion',
            field=models.TextField(default='', verbose_name='Documentacion'),
        ),
        migrations.AddField(
            model_name='ubications',
            name='img',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='ubications',
            name='tramites',
            field=models.TextField(default='', verbose_name='Tramites'),
        ),
        migrations.AlterField(
            model_name='ubications',
            name='altitud',
            field=models.DecimalField(decimal_places=16, max_digits=1000, verbose_name='Altitud'),
        ),
        migrations.AlterField(
            model_name='ubications',
            name='latitud',
            field=models.DecimalField(decimal_places=16, max_digits=1000, verbose_name='Latitud'),
        ),
    ]
