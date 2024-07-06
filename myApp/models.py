from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from accounts .models import Author

## create new user ---> create new empty profile


class Playlist(models.Model):
    author = models.ForeignKey(Author,  on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    playlist_image  = models.ImageField(upload_to='profile/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
class Video(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    image  = models.ImageField(upload_to='profile/',null=True,blank=True)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title    


class Comment(models.Model):
    user = models.ForeignKey(Author,  on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE,)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.video.title      