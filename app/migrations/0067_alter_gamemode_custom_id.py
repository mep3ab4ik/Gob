# Generated by Django 3.2.15 on 2022-10-12 12:42

from django.db import migrations, models


def handle_null_values(apps, schema_editor):
    GameMode = apps.get_model('app', 'GameMode')
    i = 1
    for game_mode in GameMode.objects.filter(custom_id__isnull=True):
        game_mode.custom_id = f'GM{i}'
        game_mode.save()
        i += 1


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0066_game_mode_custom_id_1'),
    ]

    operations = [
        migrations.RunPython(handle_null_values, reverse_code=lambda x, y: None),  # make this migration reversible
        migrations.AlterField(
            model_name='gamemode',

            name='custom_id',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]