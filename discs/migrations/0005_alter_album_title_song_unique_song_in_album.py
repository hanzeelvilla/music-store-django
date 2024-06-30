# Generated by Django 4.2.13 on 2024-06-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discs', '0004_albumformat_unique_album_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AddConstraint(
            model_name='song',
            constraint=models.UniqueConstraint(fields=('title', 'album'), name='unique_song_in_album'),
        ),
    ]
