# Generated by Django 3.2.8 on 2021-10-30 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_registering_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registering',
            name='confirm_your_password',
        ),
    ]