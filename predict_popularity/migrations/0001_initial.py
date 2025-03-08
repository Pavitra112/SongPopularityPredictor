# Generated by Django 4.2.4 on 2023-10-06 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0002_alter_userprofileinfo_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Popularity_Predictions",
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
                ("Title", models.CharField(max_length=50)),
                ("Artist", models.CharField(max_length=25)),
                ("Year", models.IntegerField()),
                ("bpm", models.IntegerField()),
                ("Energy", models.IntegerField()),
                ("Loudness", models.IntegerField()),
                ("Duration", models.IntegerField()),
                ("Acousticness", models.IntegerField()),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="popularitypredict",
                        to="accounts.userprofileinfo",
                    ),
                ),
            ],
        ),
    ]
