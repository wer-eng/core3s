# Generated by Django 3.2.5 on 2021-11-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobstable',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='session',
            name='session',
            field=models.CharField(default='2021-2022', max_length=10, unique=True),
        ),
    ]
