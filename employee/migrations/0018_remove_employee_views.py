# Generated by Django 3.1.7 on 2021-08-24 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_auto_20210824_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='views',
        ),
    ]
