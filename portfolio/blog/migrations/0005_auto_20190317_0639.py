# Generated by Django 2.1.7 on 2019-03-17 01:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190317_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 17, 1, 9, 57, 722203, tzinfo=utc)),
        ),
    ]