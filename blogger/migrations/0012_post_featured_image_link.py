# Generated by Django 3.1 on 2020-09-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0011_auto_20200923_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image_link',
            field=models.TextField(blank=True, default='', max_length=10000),
        ),
    ]
