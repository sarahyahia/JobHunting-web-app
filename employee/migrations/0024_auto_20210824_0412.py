# Generated by Django 3.1.7 on 2021-08-24 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0023_auto_20210824_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_status',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Closed')], max_length=50),
        ),
    ]
