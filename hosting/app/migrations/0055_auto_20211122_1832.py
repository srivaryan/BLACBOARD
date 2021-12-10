# Generated by Django 3.2.8 on 2021-11-22 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_remove_todo_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppCourse',
            fields=[
                ('ccode', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'app_course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AppDepartment',
            fields=[
                ('dept', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'app_department',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AppPYQ',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('q_year', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(max_length=300)),
                ('qtype', models.CharField(max_length=3)),
                ('ccode', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.appcourse')),
            ],
        ),
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['aname'],
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('NF', 'Non-Fiction'), ('F', 'Fiction'), ('Th', 'Thriller'), ('AA', 'Acrion and Adventure'), ('C', 'Comic'), ('BG', 'Biographies and Autobiographies'), ('CLB', 'College Level Books')], default='CLB', max_length=100)),
                ('available', models.BooleanField(default=True)),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('author', models.ManyToManyField(to='app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.books')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.books')),
                ('lender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='hi',
        ),
        migrations.AddField(
            model_name='appcourse',
            name='dept',
            field=models.ForeignKey(blank=True, db_column='dept', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.appdepartment'),
        ),
    ]
