# Generated by Django 3.2.8 on 2021-11-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_remove_linklession_period_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='linklession',
            name='period_no',
            field=models.IntegerField(default=1),
        ),
    ]
