# Generated by Django 3.1.6 on 2021-02-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210209_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerpath',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='trainerpath',
            name='second_feature_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='trainerpath',
            name='third_feature_name',
            field=models.CharField(max_length=25),
        ),
    ]
