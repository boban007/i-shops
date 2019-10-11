from django import forms

PACK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]


class CartAddPackForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PACK_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
