from django.urls import path
from .import views 

urlpatterns = [
    path('',views.index, name="index"),
    path('weather/',views.weather, name="weather"),
    path('news/',views.news, name="news" ),
    path('music/',views.music, name="music"),
    path('videoplayer/',views.videoplayer,name="videoplayer"),
    path('chat/',views.chatroom, name="chatroom"),
    path('chat/<str:room_name>/', views.room, name="room"),
    path('guess_game/', views.guess_game, name='guess_game')
]