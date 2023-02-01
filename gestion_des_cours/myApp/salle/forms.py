from django import forms
from myApp.models import Salle


class SalleForm (forms.ModelForm, forms.Form):

    class Meta:
        model = Salle
        fields = ('name',)

    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom de la salle',
            'class': 'form-control'
        }
    ))


class RowSalleForm(forms.Form):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom de la salle',
            'class': 'form-control'
        }
    ))
