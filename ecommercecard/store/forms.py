from urllib import request

from .models import ShippingAddress
from django import forms

class ShippingAddressForm(forms.ModelForm):

    firstname_customer = forms.CharField(required=True,label='نام سفارش دهنده')
    lastname_customer = forms.CharField(required=True, label='نام خانوادگی سفارش دهنده')
    street_address = forms.CharField(required=True, label='آدرس خیابان ')
    city = forms.CharField(required=True, label='شهر ')
    county = forms.CharField(required=True, label='شهرستان ')
    state = forms.CharField(required=True, label='استان')
    postal_code = forms.CharField(required=True, label='کدپستی')
    class Meta:
        model=ShippingAddress
        fields=['firstname_customer','lastname_customer','state','county','city','street_address','postal_code']