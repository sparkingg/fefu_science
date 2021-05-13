# Generated by Django 3.1.7 on 2021-05-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20210504_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='bibliographic_description',
            field=models.TextField(blank=True, verbose_name='Материалы конференции (полное библиографическое описание)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='financing_amount',
            field=models.FloatField(blank=True, verbose_name='Финансирование (руб.)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='financing_source',
            field=models.CharField(blank=True, max_length=300, verbose_name='Финансирование (фонд, организация)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='participants',
            field=models.IntegerField(blank=True, verbose_name='Число участников (всего)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='participants_country',
            field=models.CharField(blank=True, max_length=50, verbose_name='Участие зарубежных специалистов (страна)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='participants_foreign',
            field=models.IntegerField(blank=True, verbose_name='Участие зарубежных специалистов (всего)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='participants_university',
            field=models.IntegerField(blank=True, verbose_name='Число участников (сотрудники, учащиеся ДВФУ)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='publications_url',
            field=models.URLField(blank=True, verbose_name='Ссылки на публикации о мероприятии'),
        ),
    ]