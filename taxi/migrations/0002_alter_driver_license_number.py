# Generated by Django 4.2.2 on 2023-07-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
