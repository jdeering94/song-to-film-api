# Generated by Django 4.0.4 on 2022-04-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('spotify_link', models.CharField(max_length=200)),
            ],
        ),
    ]
