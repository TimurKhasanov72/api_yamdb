# Generated by Django 2.2.16 on 2022-10-05 17:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 5, 17, 40, 49, 590311, tzinfo=utc)),
        ),
    ]