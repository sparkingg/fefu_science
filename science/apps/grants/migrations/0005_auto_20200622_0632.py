# Generated by Django 3.0.6 on 2020-06-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0004_auto_20200622_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grant',
            name='grant_manager',
        ),
        migrations.AddField(
            model_name='grant',
            name='manager',
            field=models.CharField(default='Ivan I.', max_length=100, verbose_name='Руководитель гранта'),
            preserve_default=False,
        ),
    ]
