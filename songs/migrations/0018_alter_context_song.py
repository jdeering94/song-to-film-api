# Generated by Django 4.0.4 on 2022-04-24 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0017_alter_context_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.song'),
        ),
    ]