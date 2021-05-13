# Generated by Django 3.0.6 on 2020-06-15 09:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['description'], 'verbose_name': 'Сборник', 'verbose_name_plural': 'Сборники'},
        ),
        migrations.AlterField(
            model_name='collection',
            name='edition',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Тираж'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='isbn',
            field=models.CharField(max_length=25, validators=[django.core.validators.RegexValidator('^(?:ISBN(?:-1[03])?:? )?(?=[0-9X]{10}$|(?=(?:[0-9]+[- ]){3})[- 0-9X]{13}$|97[89][0-9]{10}$|(?=(?:[0-9]+[- ]){4})[- 0-9]{17}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9X]$')], verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='publisher',
            field=models.CharField(max_length=100, verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='volume',
            field=models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='volume_employees',
            field=models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем (выполненный штатными преподавателями)'),
        ),
    ]