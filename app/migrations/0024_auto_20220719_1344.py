# Generated by Django 3.2.14 on 2022-07-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_customdecktocard_edition'),
    ]

    operations = [
        migrations.AddField(
            model_name='customdeck',
            name='player_cards',
            field=models.ManyToManyField(
                through='app.CustomDeckToCard', to='app.PlayerCard'
            ),
        ),
        migrations.AddField(
            model_name='customdecktocard',
            name='player_card',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='player_card_to_custom_deck',
                to='app.playercard',
            ),
        ),
    ]
