# Generated by Django 3.2.15 on 2022-10-07 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_gamemode_deal_damage_to_avatar_on_empty_deck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='room_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='card',
            name='custom_id',
            field=models.CharField(default='0', max_length=64, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='control',
            name='tile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='control', to='app.tile'),
        ),
        migrations.CreateModel(
            name='BlockedCardsInGameMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_cards', to='app.card')),
                ('game_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_cards', to='app.gamemode')),
            ],
            options={
                'verbose_name': 'Blocked cards',
                'verbose_name_plural': 'Blocked cards',
            },
        ),
        migrations.AddIndex(
            model_name='blockedcardsingamemode',
            index=models.Index(fields=['game_mode'], name='blocked_cards_in_game_mode_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='blockedcardsingamemode',
            unique_together={('game_mode', 'card')},
        ),
    ]
