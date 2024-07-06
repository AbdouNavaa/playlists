
from django.urls import include, path

from . import views

app_name='accounts'

urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('login/',views.login , name='login'),
    path('logout/',views.logout , name='logout'),
    path('profile',views.profile , name='profile1'),
    path('profile/edit',views.profile_edit , name='profile_edit'),

    path('authors',views.authors , name='authors'),
    path('<str:slug>',views.profile1 , name='profile'),
]