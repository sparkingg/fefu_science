# Generated by Django 3.1.7 on 2021-05-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20210504_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='bibliographic_description',
            field=models.TextField(blank=True, null=True, verbose_name='Материалы конференции (полное библиографическое описание)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='financing_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Финансирование (руб.)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='financing_source',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Финансирование (фонд, организация)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='journal_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Указать название журнала, сборника, если планируется индексация материалов в БД Scopus'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='participants',
            field=models.IntegerField(blank=True, null=True, verbose_name='Число участников (всего)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='participants_country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Участие зарубежных специалистов (страна)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='participants_foreign',
            field=models.IntegerField(blank=True, null=True, verbose_name='Участие зарубежных специалистов (всего)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='participants_university',
            field=models.IntegerField(blank=True, null=True, verbose_name='Число участников (сотрудники, учащиеся ДВФУ)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='publications_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылки на публикации о мероприятии'),
        ),
    ]
