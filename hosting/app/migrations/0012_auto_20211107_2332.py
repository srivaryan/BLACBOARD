# Generated by Django 3.2.8 on 2021-11-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_registering_registerings'),
    ]

    operations = [
        migrations.CreateModel(
            name='registering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=2024, max_length=4, null=True)),
                ('branch', models.CharField(default='CSE', max_length=3)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=20)),
                ('confirm_your_password', models.CharField(default=' ', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='registerings',
        ),
    ]
