# Generated by Django 3.2.12 on 2022-06-14 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_card_warcry_requires_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='warcry_requires_target',
        ),
    ]
