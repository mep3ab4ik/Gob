# Generated by Django 3.2.12 on 2022-06-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_analytics_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameMode',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('battlefield_timer_duration', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Game Mode',
                'verbose_name_plural': 'Game Modes',
            },
        ),
    ]
