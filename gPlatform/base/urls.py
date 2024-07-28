from django.urls import path
from . import views

urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("<int:game_id>/rooms/", views.room_list, name="room_list"),
    path(
        "<int:game_id>/rooms/<int:room_id>/",
        views.room_detail,
        name="room_detail",
    ),
]
