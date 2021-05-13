# Generated by Django 3.0.6 on 2020-06-22 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0002_auto_20200622_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarships.ScholarshipCategory', verbose_name='Категория поддержки'),
        ),
    ]
