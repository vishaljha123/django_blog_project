# Generated by Django 3.0.2 on 2020-01-18 17:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 1, 18, 17, 17, 39, 521922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 18, 17, 17, 39, 519915, tzinfo=utc)),
        ),
    ]
