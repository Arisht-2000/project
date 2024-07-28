from django.db import models


# Create your models here.
"""
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    register_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = "用户"


class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_token"
        verbose_name = "用户token"
        verbose_name_plural = "用户token"
"""


class Game(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    # max_players = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "game"
        verbose_name = "游戏"
        verbose_name_plural = "游戏"


class Room(models.Model):
    room_id = models.CharField(max_length=255)
    desc = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    max_players = models.IntegerField()
    current_players = models.IntegerField()
    game_state = models.JSONField(default=dict)

    def __str__(self):
        return self.room_id

    class Meta:
        db_table = "room"
        verbose_name = "房间"
        verbose_name_plural = "房间"


class Player(models.Model):
    username = models.CharField(max_length=20)
    symbol = models.CharField(max_length=1, default="")
    # password = models.CharField(max_length=20)
    # email = models.EmailField()
    # phone = models.CharField(max_length=11)
    # register_time = models.DateTimeField(auto_now_add=True)
    # last_login_time = models.DateTimeField(auto_now=True)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "player"
        verbose_name = "玩家"
        verbose_name_plural = "玩家"
