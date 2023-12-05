# Generated by Django 3.2.15 on 2022-09-12 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_enchantment_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='status',
            field=models.CharField(blank=True, choices=[('online', 'Online'), ('offline', 'Offline'), ('away', 'Away'), ('in_battle', 'In battle')], max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
