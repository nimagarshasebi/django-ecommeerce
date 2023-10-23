from django.urls import path
from .views import customerprofile,registercustomer,CustomerLogin,make_user_address,showaddress,set_default_address,CustomerPasswordReset,PasswordResetConfirmView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/',customerprofile,name='profile'),
    path('register/',registercustomer,name='register'),
    path('login/',CustomerLogin.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('add-address/',make_user_address,name='add-address'),
    path('address/',showaddress,name='address'),
    path('set-default-address/', set_default_address, name='set-default-address'),
    path('password-reset/',CustomerPasswordReset.as_view(template_name='users/password_reset.html',html_email_template_name='users/password_reset_email.html'),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),

]
