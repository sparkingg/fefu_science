# Generated by Django 3.0.5 on 2020-05-08 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0003_conference_conference_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conferencetype',
            options={'verbose_name': 'Conference Type', 'verbose_name_plural': 'Conference Types'},
        ),
    ]
