# Generated by Django 3.2.8 on 2021-11-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_alter_lesson_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='gmeet_link',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
