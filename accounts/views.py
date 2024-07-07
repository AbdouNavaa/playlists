from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render,get_object_or_404
from .forms import SignUpForm , UserForm , ProfileForm, LogInForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Author
from django.urls import reverse
from myApp .models import Playlist, Video

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile_image = form.cleaned_data.get('profile_image')
            author = Author.objects.create(user=user, image=profile_image)
            auth_login(request, user)
            return redirect('accounts:authors')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})




def login(request):
    if request.method == 'POST':
        form = LogInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                next_url = request.POST.get('next', 'accounts:authors')
                return redirect('accounts:profile')
            else:
                print('Authentication failed')
        else:
            print(form.errors)
    else:
        form = LogInForm()

    return render(request, 'registration/login.html', {'form': form, 'next': request.GET.get('next', '')})


def logout(request):
    auth_logout(request)
    return render(request, 'registration/login.html',{})



def profile(request):
    profile = Author.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})

def authors(request):
    authors = Author.objects.all()

    context = {'authors' :authors , } # template name
    return render(request,'authors.html',context)



from django.http import HttpResponse

@login_required
def test_login(request):
    return HttpResponse(f"User: {request.user.username}, Authenticated: {request.user.is_authenticated}")

from django.contrib.auth.models import User

@login_required
def profile1(request):
    print('Auth: Start')
    # try:
    user_id = request.user.id
    print('hello:',user_id)     
    author = Author.objects.get(user=request.user.id)
    # print('Auth:', author.user.username)
    context = {'author': author}
    return render(request, 'profile.html', context)


def teacher_profile(request , slug):
    author = Author.objects.get(slug=slug)
    playlists = Playlist.objects.filter(author=author)
    context = {'author' : author,'playlists':playlists }
    return render(request,'teacher_profile.html',context)

def profile_edit(request):
    profile = Author.objects.get(user=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})