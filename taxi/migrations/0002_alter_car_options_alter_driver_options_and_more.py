# Generated by Django 4.1 on 2023-09-20 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ["model"]},
        ),
        migrations.AlterModelOptions(
            name="driver",
            options={
                "ordering": ["last_name"],
                "verbose_name": "driver",
                "verbose_name_plural": "drivers",
            },
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ["name"]},
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="taxi.manufacturer",
            ),
        ),
    ]