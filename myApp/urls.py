from django.urls import include, path

from . import views


app_name='myApp'

urlpatterns = [
    path('',views.home , name='home'),
    path('courses',views.courses , name='courses'),
    path('P<int:id>',views.playlists , name='playlists'),
    path('V<int:id>',views.watch_video , name='watch_video'),
    path('add_playlist/', views.add_playlist, name='add_playlist'),
    path('add_video/<int:id>/', views.add_video, name='add_video'),
]