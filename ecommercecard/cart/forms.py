from django import forms
PRODUCT_COUNT_CHOICES=[(i,str(i)) for i in range(1,9)]
class CartAddProductForm(forms.Form):
    product_count=forms.TypedChoiceField(choices=PRODUCT_COUNT_CHOICES,coerce=int,label="",widget=forms.Select(attrs={'class': 'input-number__input form-control form-control-lg'}))
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput())


