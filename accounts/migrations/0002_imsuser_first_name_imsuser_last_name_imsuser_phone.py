# Generated by Django 4.2.3 on 2023-09-22 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imsuser',
            name='first_name',
            field=models.CharField(default='hello', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imsuser',
            name='last_name',
            field=models.CharField(default='world', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imsuser',
            name='phone',
            field=models.CharField(default='1234', max_length=13, verbose_name='Phone Number'),
            preserve_default=False,
        ),
    ]
