# Generated by Django 5.0.7 on 2024-07-24 17:35

import location_field.models.plain
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
