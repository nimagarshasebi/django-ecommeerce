
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class UpdateProfile(forms.ModelForm):
    phone_number=forms.CharField(required=False,label='شماره همراه')
    first_name=forms.CharField(required=False,label='نام')
    last_name =forms.CharField(required=False, label='نام خانوادگی')
    username = forms.CharField(required=True, label='نام کاربری')
    email = forms.EmailField(required=True, label='آدرس ایمیل')
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','phone_number']



class RegisterCustomer(UserCreationForm):
    email=forms.EmailField(required=False, label='آدرس ایمیل')
    username =forms.CharField(required=False, label='نام کاربری')
    password1=forms.CharField(required=False,widget=forms.PasswordInput,label='رمزعبور')
    password2 = forms.CharField(required=False, widget=forms.PasswordInput, label='تکراررمزعبور')

    class Meta:
        model=User
        fields=['username','email','password1','password2']
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='نام کاربری',widget=forms.TextInput())
    password = forms.CharField(label='رمزعبور',widget=forms.PasswordInput())


