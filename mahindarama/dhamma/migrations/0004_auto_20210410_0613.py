# Generated by Django 3.2 on 2021-04-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhamma', '0003_alter_dhamma_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhamma',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sangha',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]