# Generated by Django 3.2 on 2021-04-13 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dhamma', '0004_auto_20210410_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dhamma',
            name='record_date',
        ),
    ]
