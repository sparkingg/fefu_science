# Generated by Django 3.0.6 on 2020-06-07 08:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_auto_20200607_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Code'),
        ),
    ]
