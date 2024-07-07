from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import PlaylistForm, VideoForm
# Create your views here.
def home(request ):
    authors = User.objects.all()
    cours = Playlist.objects.all()
    context = {'authors' : authors, 'cours': cours }
    return render(request,'home.html',context)


def courses(request ):
    cours = Playlist.objects.all()
    context = {'cours': cours }
    return render(request,'courses.html',context)

def playlists(request, id):
    videos = Video.objects.filter(playlist=id)
    playlist = Playlist.objects.get(id=id)
    context = {'videos' :videos, 'playlist':playlist  } # template name
    return render(request,'playlist.html',context)

def watch_video(request,id):
    video = Video.objects.get(id=id)
    comment = Comment.objects.filter(video=video)
    return render(request, 'watch-video.html',{'video':video,'comment':comment})


def add_like(request,id):
    video = Video.objects.get(id=id)
    video.playlist.author.total_likes += 1  # Increment the author's total_likes
    video.likes += 1  # Increment the video's likes
    video.save()
    video.playlist.author.save()
    comment = Comment.objects.filter(video=video)
    return render(request, 'watch-video.html',{'video':video,'comment':comment})

from django.contrib.auth.decorators import login_required


@login_required
def add_comment(request, v_id):
    video = get_object_or_404(Video, id=v_id)

    try:
        author = Author.objects.get(user=request.user)
        print('ok')
    except Author.DoesNotExist:
        print('no')
        
        # Gérer le cas où l'utilisateur connecté n'a pas de profil Author
        return redirect('profile_creation_url')  # Rediriger vers une page de création de profil ou afficher un message d'erreur

    if request.method == 'POST':
        print('ok1')
        description = request.POST.get('comment_box', '')
        if description:
            # Créer et sauvegarder le commentaire
            Comment.objects.create(
                user=author,
                video=video,
                description=description
            )
            # Incrémenter le nombre de commentaires de l'auteur
            author.total_comments += 1
            author.save()

    # Récupérer les commentaires associés à la vidéo
    comments = Comment.objects.filter(video=video)

    return render(request, 'watch-video.html', {'video': video, 'comments': comments})

def add_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            print('OK')
            playlist = form.save(commit=False)
            # playlist_id = playlist.id
            playlist.save()
            print('playlist_id:',playlist.id)
            author = Author.objects.get(pk=form.cleaned_data['author'].id)
            playlist = Playlist.objects.all()
            # videos = Video.objects.filter(playlist=playlist)
            author.total_palylist += 1  # Increment the author's total_videos
            author.save()  # Save the changes to the author
            # context = { 'playlist':playlist  }
            return redirect('myApp:home', )
            # return render(request,'courses.html',context)

    else:
        print('No')
        form = PlaylistForm()
    return render(request, 'add_playlist.html', {'form': form})

def add_video(request, id):
    print('here1')
    playlist =Playlist.objects.get(id=id)
    print('here2')
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            print('ok')
            video = form.save(commit=False)
            video.playlist = playlist
            video.save()
            playlist.author.total_videos += 1  # Increment the author's total_videos
            playlist.total_videos += 1  # Increment the author's total_videos
            playlist.author.save()  # Save the changes to the author
            playlist.author.save()  # Save the changes to the author
            return redirect('myApp:playlists', id=playlist.id)
    else:
        print('no')
        form = VideoForm()
    return render(request, 'add_video.html', {'form': form, 'playlist': playlist})