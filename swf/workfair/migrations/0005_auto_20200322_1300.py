# Generated by Django 3.0.4 on 2020-03-22 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workfair', '0004_vacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.TextField(max_length=32),
        ),
    ]
