# Generated by Django 3.0.6 on 2020-06-08 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contests',
            old_name='contest_name',
            new_name='contest',
        ),
        migrations.RenameField(
            model_name='contests',
            old_name='project_name',
            new_name='project',
        ),
    ]