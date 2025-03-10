# Generated by Django 4.2.4 on 2023-10-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict_popularity", "0002_remove_popularity_predictions_duration_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="popularity_predictions",
            name="Danceability",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="popularity_predictions",
            name="Duration",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="popularity_predictions",
            name="Liveness",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="popularity_predictions",
            name="Speechiness",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="popularity_predictions",
            name="Valence",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="popularity_predictions",
            name="Acousticness",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="popularity_predictions",
            name="Energy",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="popularity_predictions",
            name="Loudness",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="popularity_predictions",
            name="bpm",
            field=models.IntegerField(default=0),
        ),
    ]
