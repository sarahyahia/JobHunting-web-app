# Generated by Django 3.1.7 on 2021-08-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0021_merge_20210824_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(default=0, editable=False, primary_key=True, serialize=False),
        ),
    ]
