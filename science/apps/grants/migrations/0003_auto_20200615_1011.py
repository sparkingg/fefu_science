# Generated by Django 3.0.6 on 2020-06-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0002_auto_20200615_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='project',
            field=models.CharField(max_length=200, verbose_name='Название проекта'),
        ),
    ]
