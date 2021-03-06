# Generated by Django 3.0.6 on 2020-06-08 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('publisher', models.CharField(max_length=100, verbose_name='Publisher')),
                ('isbn', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator('^\n                (?:ISBN(?:-1[03])?:?\\ )?  # Optional ISBN/ISBN-10/ISBN-13 identifier.\n                (?=                       # Basic format pre-checks (lookahead):\n                  [0-9X]{10}$             #   Require 10 digits/Xs (no separators).\n                 |                        #  Or:\n                  (?=(?:[0-9]+[-\\ ]){3})  #   Require 3 separators\n                  [-\\ 0-9X]{13}$          #     out of 13 characters total.\n                 |                        #  Or:\n                  97[89][0-9]{10}$        #   978/979 plus 10 digits (13 total).\n                 |                        #  Or:\n                  (?=(?:[0-9]+[-\\ ]){4})  #   Require 4 separators\n                  [-\\ 0-9]{17}$           #     out of 17 characters total.\n                )                         # End format pre-checks.\n                (?:97[89][-\\ ]?)?         # Optional ISBN-13 prefix.\n                [0-9]{1,5}[-\\ ]?          # 1-5 digit group identifier.\n                [0-9]+[-\\ ]?[0-9]+[-\\ ]?  # Publisher and title identifiers.\n                [0-9X]                    # Check digit.\n                $')], verbose_name='ISBN')),
                ('edition', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Edition')),
                ('volume', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Volume')),
                ('volume_employees', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Volume (Full-time university employees)')),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
                'ordering': ['description'],
            },
        ),
    ]
