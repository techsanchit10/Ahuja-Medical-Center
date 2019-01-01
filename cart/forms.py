from django import forms


TEST_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 2)]


class CartAddTestForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=TEST_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
