# Generated by Django 4.0.1 on 2022-01-27 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_movement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_movement',
            name='Date',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]