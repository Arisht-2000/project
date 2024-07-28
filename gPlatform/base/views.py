from django.shortcuts import render

# Create your views here.
from .models import Game, Room, Player


def game_list(request):
    games = Game.objects.all()
    return render(request, "base/game_list.html", {"games": games})


def room_list(request, game_id):
    game = Game.objects.get(id=game_id)
    rooms = Room.objects.filter(game=game)
    return render(request, "base/room_list.html", {"rooms": rooms, "game": game})


def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    players = Player.objects.filter(room=room)
    return render(
        request,
        "base/room_detail.html",
        {"room": room, "players": players},
    )
