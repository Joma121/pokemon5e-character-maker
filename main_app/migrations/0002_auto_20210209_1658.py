# Generated by Django 3.1.6 on 2021-02-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerpath',
            name='description',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='trainerpath',
            name='first_description',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='trainerpath',
            name='second_description',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='trainerpath',
            name='third_description',
            field=models.TextField(max_length=700),
        ),
    ]
