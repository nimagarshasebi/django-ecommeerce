
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Address

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


class AddressForm(forms.ModelForm):
    firstname_customer = forms.CharField(required=True,label='نام سفارش دهنده')
    lastname_customer = forms.CharField(required=True, label='نام خانوادگی سفارش دهنده')
    street_address = forms.CharField(required=True, label='آدرس خیابان ')
    city = forms.CharField(required=True, label='شهر ')
    county = forms.CharField(required=True, label='شهرستان ')
    state = forms.CharField(required=True, label='استان')
    postal_code = forms.CharField(required=True, label='کدپستی')

    class Meta:
        model=Address
        fields=['firstname_customer','lastname_customer','state','county','city','street_address','postal_code']


class DefaultAddressButton(forms.ModelForm):
    address_id = forms.IntegerField(widget=forms.HiddenInput())
    default_address = forms.BooleanField(required=False, initial=False)
    class Meta:
        model=Address
        fields=['default_address','address_id']