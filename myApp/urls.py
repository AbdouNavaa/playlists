from django.urls import include, path

from . import views


app_name='myApp'

urlpatterns = [
    path('',views.home , name='home'),
    path('courses',views.courses , name='courses'),
    path('P<int:id>',views.playlists , name='playlists'),
    path('V<int:id>',views.watch_video , name='watch_video'),
    path('<int:id>/<int:c_id>',views.to_Update , name='to_Update'),
    path('add_playlist/', views.add_playlist, name='add_playlist'),
    path('add_video/<int:id>/', views.add_video, name='add_video'),
    path('add_like/<int:id>/', views.add_like, name='add_like'),
    path('update_comment/<int:v_id>/<int:c_id>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:v_id>/<int:c_id>', views.delete_comment, name='delete_comment'),
    path('add_comment/<int:v_id>/', views.add_comment, name='add_comment'),
]