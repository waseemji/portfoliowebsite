# Generated by Django 4.1 on 2022-12-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMe",
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
                ("user_name", models.CharField(max_length=100)),
                ("user_email", models.EmailField(max_length=254)),
                ("subject", models.TextField()),
                ("user_message", models.TextField()),
            ],
        ),
    ]
