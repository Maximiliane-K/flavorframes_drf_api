# Generated by Django 3.2.25 on 2024-12-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='images/default_post_u8igak', upload_to='images/'),
        ),
    ]
