# Generated by Django 3.0.6 on 2020-06-16 04:16

import apps.common.models
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Guide Category',
                'verbose_name_plural': 'Guide Categories',
            },
        ),
        migrations.CreateModel(
            name='ManualCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Manual Category',
                'verbose_name_plural': 'Manual Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='textbook',
            options={'verbose_name': 'Textbook', 'verbose_name_plural': 'Textbooks'},
        ),
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('publisher', models.CharField(blank=True, max_length=100, verbose_name='Издатель')),
                ('circulation', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Circulation')),
                ('isbn', apps.common.models.ISBNField(blank=True, max_length=25, verbose_name='ISBN')),
                ('volume', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем')),
                ('volume_employees', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем (выполненный штатными преподавателями)')),
                ('employee_authors', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, size=None, verbose_name='Авторы (сотрудники)')),
                ('foreign_authors', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, size=None, verbose_name='Авторы (иностранцы)')),
                ('postgraduate_authors', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, size=None, verbose_name='Авторы (аспиранты, докторанты)')),
                ('student_authors', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, size=None, verbose_name='Авторы (студенты)')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textbooks.ManualCategory', verbose_name='Категория')),
                ('field_of_study', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='textbooks.FieldOfStudy', verbose_name='Field of Study')),
            ],
            options={
                'verbose_name': 'Manual',
                'verbose_name_plural': 'Manuals',
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('publisher', models.CharField(blank=True, max_length=100, verbose_name='Издатель')),
                ('circulation', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Circulation')),
                ('isbn', apps.common.models.ISBNField(blank=True, max_length=25, verbose_name='ISBN')),
                ('volume', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем')),
                ('volume_employees', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем (выполненный штатными преподавателями)')),
                ('employee_authors', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, size=None, verbose_name='Авторы (сотрудники)')),
                ('foreign_authors', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, size=None, verbose_name='Авторы (иностранцы)')),
                ('postgraduate_authors', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, size=None, verbose_name='Авторы (аспиранты, докторанты)')),
                ('student_authors', django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, size=None, verbose_name='Авторы (студенты)')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textbooks.GuideCategory', verbose_name='Категория')),
                ('field_of_study', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='textbooks.FieldOfStudy', verbose_name='Field of Study')),
            ],
            options={
                'verbose_name': 'Guide',
                'verbose_name_plural': 'Guides',
            },
        ),
    ]
