# Generated by Django 4.0.4 on 2022-04-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_album_film_song_album_song_films'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='films',
        ),
    ]
