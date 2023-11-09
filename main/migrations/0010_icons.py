# Generated by Django 4.2.7 on 2023-11-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_aboutus"),
    ]

    operations = [
        migrations.CreateModel(
            name="Icons",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("icon", models.CharField(max_length=100, verbose_name="icon")),
                ("text", models.TextField(verbose_name="text")),
            ],
            options={
                "verbose_name": "Icon",
                "verbose_name_plural": "Icons",
            },
        ),
    ]