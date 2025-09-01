from django.contrib import admin
from . models import Playlist
from . models import videoList

admin.site.register(Playlist)
admin.site.register(videoList)