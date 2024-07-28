# Generated by Django 5.0.7 on 2024-07-28 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("desc", models.TextField()),
            ],
            options={
                "verbose_name": "游戏",
                "verbose_name_plural": "游戏",
                "db_table": "game",
            },
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_id", models.CharField(max_length=255)),
                ("desc", models.TextField()),
                ("max_players", models.IntegerField()),
                ("current_players", models.IntegerField()),
                ("game_state", models.JSONField(default=dict)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.game"
                    ),
                ),
            ],
            options={
                "verbose_name": "房间",
                "verbose_name_plural": "房间",
                "db_table": "room",
            },
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=20)),
                ("symbol", models.CharField(default="", max_length=1)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.room"
                    ),
                ),
            ],
            options={
                "verbose_name": "玩家",
                "verbose_name_plural": "玩家",
                "db_table": "player",
            },
        ),
    ]
