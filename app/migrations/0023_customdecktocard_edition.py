# Generated by Django 3.2.14 on 2022-07-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_new_card_relation_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='customdecktocard',
            name='edition',
            field=models.CharField(
                default='regular',
                max_length=50,
                verbose_name=(('regular', 'Regular'), ('shiny', 'Shiny')),
            ),
        ),
    ]