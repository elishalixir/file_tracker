# Generated by Django 4.0.1 on 2022-01-27 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_movement', '0005_remove_file_movement_file_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_movement',
            name='File_number',
            field=models.IntegerField(default=1234),
        ),
    ]