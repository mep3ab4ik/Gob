# Generated by Django 3.2.15 on 2022-10-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_auto_20221011_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemode',
            name='custom_id',
            field=models.CharField(max_length=16, null=True),
        )
    ]