# Generated by Django 2.1.7 on 2019-03-14 20:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190313_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 14, 20, 35, 9, 4817, tzinfo=utc)),
        ),
    ]
