from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    text = forms.TextInput()
    name = forms.CharField(required=False, label='نام')
    email = forms.CharField(required=False,label='ایمیل')
    class Meta:
        model=Comment
        fields=['name','email','text']

class CartAddProductFormStore(forms.Form):
    product_count=forms.IntegerField(min_value=1, label="", initial=1, widget=forms.NumberInput(attrs={'class': "counter"}))
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput())