from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('process_register', views.process_register),
    path('create_profile', views.create_profile),
    path('process_profile', views.process_profile),
    path('login', views.login),
    path('process_login', views.process_login),
    path('logout', views.logout),
    path('user_dash', views.user_dash),
    path('user_profile', views.user_profile),
    path('profile_settings', views.profile_settings),
    path('create_post', views.create_post),
    path('feed', views.feed),
    path('user_account', views.user_account),
    path('user_analytics', views.user_analytics),
]