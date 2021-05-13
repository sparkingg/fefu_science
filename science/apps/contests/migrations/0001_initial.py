# Generated by Django 3.0.6 on 2020-06-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fond', models.CharField(max_length=50, verbose_name='Fond Name')),
                ('program', models.CharField(blank=True, max_length=200, verbose_name='Program Name')),
                ('contest_name', models.CharField(max_length=300, verbose_name='Contest Name')),
                ('project_name', models.CharField(max_length=300, verbose_name='Project Name')),
                ('project_manager', models.CharField(max_length=100, verbose_name='Project Manager (full name, position, degree, rank)')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]