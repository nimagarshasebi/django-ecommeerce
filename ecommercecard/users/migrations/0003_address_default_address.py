# Generated by Django 4.2 on 2023-09-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='default_address',
            field=models.BooleanField(default=False),
        ),
    ]
