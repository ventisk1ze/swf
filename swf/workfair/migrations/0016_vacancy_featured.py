# Generated by Django 3.0.4 on 2020-03-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workfair', '0015_auto_20200329_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
