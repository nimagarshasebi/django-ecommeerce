from django.urls import path
from .views import customerprofile,registercustomer,CustomerLogin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/',customerprofile,name='profile'),
    path('register/',registercustomer,name='register'),
    path('login/',CustomerLogin.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),


]
