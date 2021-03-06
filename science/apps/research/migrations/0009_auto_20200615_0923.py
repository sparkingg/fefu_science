# Generated by Django 3.0.6 on 2020-06-15 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0008_auto_20200608_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.Category', verbose_name='Код рубрики ГРНТИ'),
        ),
        migrations.AlterField(
            model_name='research',
            name='reasons',
            field=models.TextField(verbose_name='Основание для выполнения'),
        ),
    ]
