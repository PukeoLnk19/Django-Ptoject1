# Generated by Django 4.1 on 2022-09-14 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='update',
        ),
    ]
