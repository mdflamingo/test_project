from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.urls import path

from . import views
from .views import registration, profile

app_name = 'user'

urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='user'),
    # path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    # path('profile/', views.Profile.as_view(template_name='user/profile.html'))
    path('registration/', registration),
    path('profile/', profile)
]
