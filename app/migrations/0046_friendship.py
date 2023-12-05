# Generated by Django 3.2.15 on 2022-08-17 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_clientversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientversion',
            name='is_currently_selected',
            field=models.BooleanField(default=False, verbose_name='Is this version selected'),
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='app.player')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.player')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_friends', to='app.player')),
            ],
            options={
                'unique_together': {('friend', 'player')},
            },
        ),
    ]