# Generated by Django 3.2.15 on 2022-08-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_battle_current_turn_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enchantment',
            name='keyword',
            field=models.CharField(choices=[('warcry', 'Warcry'), ('censor', 'Censor'), ('leech', 'Leech'), ('insult', 'Insult'), ('pounce', 'Pounce'), ('barrier', 'Barrier'), ('untouchable', 'Untouchable'), ('mummy', 'Mummy'), ('ensnare', 'Ensnare'), ('mia', 'MIA'), ('tile_buff', 'Tile Buff'), ('protect', 'Protect'), ('invisible', 'Invisible')], default='warcry', max_length=100),
        ),
    ]
