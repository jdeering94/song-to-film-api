# Generated by Django 4.0.4 on 2022-04-19 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_context_song_films_context_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='films',
        ),
    ]
