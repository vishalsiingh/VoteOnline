from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views  # Import views from the 'users' app (assuming views.py is in the 'users' folder)
from .views import profile_view

urlpatterns = [
    path('', views.indexpage_view, name='landing_page'),
    path('404/', views.page404_view, name='404'),
    path('voters/profile-page/', views.votersprofile_view, name='voters_profile'),
    path('voter-homepage/', views.homepage_view, name='voters_homepage'),
    path('voters/<str:id>/aspirant/profile/<str:aspirant_name>/', views.electoralpost_view, name='voters_vie'),
    path('elect-your-leaders/<str:pk>/<str:school>', views.voting_view, name='elect_leaders'),
    path('polling/<str:pk>/school/polls/<str:school>/', views.polling_view, name='poll'),
    path('poll-results/', views.results_view, name='poll_results'),
    path('election-results/', views.election_results_view, name='election_results'),
path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout_user'),
 path('logout/', views.custom_logout, name='logout_user'),
 path('users-profile/', views.profile_view, name='profile_page'),
path('users-profile/', profile_view, name='profile_page'),
    path('official-profile/', views.officials_profile_view, name='official_profile'),
    path('homepage/', views.officials_homepage, name='official_homepage'),
    path('nomination/', views.nominate_aspirants_view, name='nominate_aspirants'),
    path('aspirants-info/nominated-aspirants/', views.display_nominated_aspirants_view, name='view_nominated_aspirants'),

]
