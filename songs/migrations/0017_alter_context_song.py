# Generated by Django 4.0.4 on 2022-04-24 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0016_alter_song_films'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='song',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='songs.song'),
        ),
    ]
