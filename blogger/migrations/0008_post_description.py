# Generated by Django 3.1 on 2020-09-23 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0007_auto_20200923_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
    ]
