from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','user','total_palylist','total_videos','total_likes', 'total_comments')

admin.site.register(Author,AuthorAdmin)
