# Generated by Django 3.2.25 on 2025-02-28 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_eventattendance_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventattendance',
            name='test_field',
        ),
    ]
