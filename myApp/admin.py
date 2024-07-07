from django.contrib import admin
from .models import *

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','title','likes')

class ComAdmin(admin.ModelAdmin):
    list_display = ('id','user','video')
        

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    list_display = ('id','author','title','total_videos')
    

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Comment,ComAdmin)
# admin.site.register(Playlist)
