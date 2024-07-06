from django.contrib import admin
from .models import *


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Video)
admin.site.register(Comment)
# admin.site.register(Playlist)
