# Generated by Django 4.2.7 on 2023-11-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_ourservice"),
    ]

    operations = [
        migrations.CreateModel(
            name="OurGallery",
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
                ("title", models.CharField(max_length=50, verbose_name="Title")),
                ("subtitle", models.CharField(max_length=50, verbose_name="SubTitle")),
                (
                    "img_small",
                    models.ImageField(upload_to="media", verbose_name="Small Image"),
                ),
                (
                    "img_large",
                    models.ImageField(upload_to="media", verbose_name="Large Image"),
                ),
            ],
            options={
                "verbose_name": "Our Gallery",
                "verbose_name_plural": "Our Galleries",
            },
        ),
    ]
