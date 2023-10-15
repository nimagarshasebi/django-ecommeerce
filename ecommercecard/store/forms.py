from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    text = forms.TextInput()
    name = forms.CharField(required=False, label='نام')
    email = forms.CharField(required=False,label='ایمیل')
    class Meta:
        model=Comment
        fields=['name','email','text']

