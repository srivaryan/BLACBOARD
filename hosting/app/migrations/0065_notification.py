# Generated by Django 3.2.8 on 2021-11-28 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0064_remove_post_post_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('response', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.books', unique=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
