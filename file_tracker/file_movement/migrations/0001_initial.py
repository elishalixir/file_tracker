# Generated by Django 4.0.1 on 2022-01-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='file_movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('File_number', models.IntegerField(max_length=5)),
                ('Project_title', models.CharField(max_length=200)),
                ('Proponent', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=100)),
                ('Action', models.CharField(max_length=100)),
            ],
        ),
    ]
