# Generated by Django 3.2.8 on 2021-11-17 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20211117_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='day',
            new_name='period_day',
        ),
    ]
