# Generated by Django 3.0.6 on 2020-06-15 11:22

import apps.common.models
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Scholarship Category',
                'verbose_name_plural': 'Scholarship Categories',
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('activity', models.CharField(blank=True, max_length=250, verbose_name='Activity Name')),
                ('project', models.CharField(blank=True, max_length=300, verbose_name='Название проекта')),
                ('time_period', models.CharField(blank=True, max_length=50, verbose_name='Time Period')),
                ('financing', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Financing')),
                ('participants', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), size=None, verbose_name='Participants')),
                ('support_type', models.CharField(max_length=100, verbose_name='Support Type')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarships.ScholarshipCategory', verbose_name='Scholarship Category')),
            ],
            options={
                'verbose_name': 'Scholarship',
                'verbose_name_plural': 'Scholarships',
                'ordering': ['project'],
            },
        ),
    ]
