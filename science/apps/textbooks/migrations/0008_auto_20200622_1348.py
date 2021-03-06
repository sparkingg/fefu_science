# Generated by Django 3.0.6 on 2020-06-22 13:48

import apps.common.models
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0007_auto_20200622_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='employee_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (сотрудники)'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='field_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='textbooks.FieldOfStudy', verbose_name='Область исследования'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='foreign_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (иностранцы)'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='isbn',
            field=apps.common.models.ISBNField(blank=True, max_length=25, null=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='postgraduate_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (аспиранты, докторанты)'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='student_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (студенты)'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='volume_employees',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем, выполненный штантыми преподавателями'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='employee_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (сотрудники)'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='field_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='textbooks.FieldOfStudy', verbose_name='Область исследования'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='foreign_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (иностранцы)'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='isbn',
            field=apps.common.models.ISBNField(blank=True, max_length=25, null=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='postgraduate_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (аспиранты, докторанты)'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='student_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (студенты)'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='volume_employees',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем, выполненный штантыми преподавателями'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='employee_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (сотрудники)'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='field_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='textbooks.FieldOfStudy', verbose_name='Область исследования'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='foreign_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (иностранцы)'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='isbn',
            field=apps.common.models.ISBNField(blank=True, max_length=25, null=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='postgraduate_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (аспиранты, докторанты)'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='student_authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=apps.common.models.AuthorField(max_length=25), blank=True, null=True, size=None, verbose_name='Авторы (студенты)'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='volume_employees',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Объем, выполненный штантыми преподавателями'),
        ),
    ]
