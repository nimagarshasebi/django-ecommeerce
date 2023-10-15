from django import forms

class CartAddProductForm(forms.Form):
    product_count=forms.IntegerField(min_value=1,label="",initial=1,widget=forms.NumberInput(attrs={'class':'product-count'}))
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput())




