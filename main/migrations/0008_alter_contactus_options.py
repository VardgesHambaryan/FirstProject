# Generated by Django 4.2.7 on 2023-11-09 13:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_remove_contactus_subject_contactus_email"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contactus",
            options={"verbose_name": "Contact Us", "verbose_name_plural": "Contact Us"},
        ),
    ]
