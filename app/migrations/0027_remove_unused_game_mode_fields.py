# Generated by Django 3.2.14 on 2022-07-20 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_gamemodeseason_game_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamemode',
            name='ends_at',
        ),
        migrations.RemoveField(
            model_name='gamemode',
            name='starts_at',
        ),
    ]
