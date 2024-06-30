from django.contrib import admin
from .models import Genre, Format, Album, AlbumFormat, Song

admin.site.register(Genre)
admin.site.register(Format)
admin.site.register(Album)
admin.site.register(AlbumFormat)
admin.site.register(Song)