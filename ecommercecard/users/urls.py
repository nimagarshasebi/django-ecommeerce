from django.urls import path
from .views import customerprofile,registercustomer,CustomerLogin,make_user_address,showaddress
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/',customerprofile,name='profile'),
    path('register/',registercustomer,name='register'),
    path('login/',CustomerLogin.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('add-address/',make_user_address,name='add-address'),
    path('address/',showaddress,name='address'),
    #path('bbb/',set_default_address,name='bbb')
]
