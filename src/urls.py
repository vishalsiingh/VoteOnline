from django.contrib import admin
from django.urls import path, include
# from . import views
# from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),
#     path('users/', include('users.urls')),
#     path(
#         'accounts/logout/',
#         auth_views.LogoutView.as_view(next_page='user_login'),  # this is the fix
#         name='logout_user'
#     ),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('users/', include('users.urls')),
 path('', lambda request: redirect('user_login')),
    # 🔁 Use the correct name and redirection target
    # path('voter/profile/', views.votersprofile_view, name='voters_profile'),

    # 
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(template_name='logout.html', next_page='user_login'),
        name='logout_user'
    ),
    # Root URL redirects to login page
    # path('', lambda request: redirect('login_user')),
    # Add this line to handle '/'
   
]
