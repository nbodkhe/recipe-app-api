# Generated by Django 3.2.23 on 2023-11-17 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_minute',
            new_name='time_minutes',
        ),
    ]
