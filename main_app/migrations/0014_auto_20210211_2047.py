# Generated by Django 3.1.6 on 2021-02-11 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20210211_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='path',
        ),
        migrations.DeleteModel(
            name='TrainerPath',
        ),
    ]