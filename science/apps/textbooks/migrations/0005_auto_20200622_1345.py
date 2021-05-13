# Generated by Django 3.0.6 on 2020-06-22 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0004_auto_20200622_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='circulation',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Тираж'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='circulation',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Тираж'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='circulation',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Тираж'),
        ),
    ]
