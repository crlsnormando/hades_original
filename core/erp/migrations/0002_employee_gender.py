# Generated by Django 4.1 on 2022-08-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
