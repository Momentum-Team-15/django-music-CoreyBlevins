# Generated by Django 4.1.2 on 2022-10-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
