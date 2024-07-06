from django import forms
from .models import Playlist, Video

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['author', 'title', 'playlist_image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','image', 'video_file', 'description']
