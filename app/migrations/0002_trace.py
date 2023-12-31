# Generated by Django 3.2.7 on 2022-04-07 13:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trace',
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
                ('error', models.CharField(max_length=200)),
                ('traceback', models.TextField()),
                ('traceback_hash', models.CharField(max_length=32)),
                (
                    'created_date',
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
