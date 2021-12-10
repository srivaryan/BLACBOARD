# Generated by Django 3.2.8 on 2021-10-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_usernmae_registering_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registering',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='registering',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registering',
            name='password',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='registering',
            name='username',
            field=models.CharField(max_length=500),
        ),
    ]