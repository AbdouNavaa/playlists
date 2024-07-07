
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('login/',views.login , name='login'),
    path('logout/',views.logout , name='logout'),
    path('profile',views.profile , name='profile1'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('authors',views.authors , name='authors'),
    path('Profile',views.profile1 , name='profile'),
    path('T<str:slug>',views.teacher_profile , name='teacher_profile'),
    path('test_login/', views.test_login, name='test_login'),
]