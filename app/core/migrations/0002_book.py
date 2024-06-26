# Generated by Django 5.0.6 on 2024-06-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("isbn", models.CharField(max_length=10)),
                ("pages", models.IntegerField()),
            ],
        ),
    ]
