# Generated by Django 3.0.6 on 2020-06-16 04:11

import apps.common.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20200615_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='isbn',
            field=apps.common.models.ISBNField(max_length=25, verbose_name='ISBN'),
        ),
    ]
