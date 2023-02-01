from django import forms
from myApp.models import Filiere


class FiliereForm (forms.ModelForm, forms.Form):

    class Meta:
        model = Filiere
        fields = ('name',)

    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom promo',
            'class': 'form-control'
        }
    ))


class RowFiliereForm(forms.Form):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom promo',
            'class': 'form-control'
        }
    ))
