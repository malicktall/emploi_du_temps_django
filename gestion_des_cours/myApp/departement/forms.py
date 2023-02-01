from django import forms
from myApp.models import Departement


class DepartementForm (forms.ModelForm, forms.Form):

    class Meta:
        model = Departement
        fields = ('name',)

    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom du Departement',
            'class': 'form-control'
        }
    ))


class RowDepartementForm(forms.Form):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom du Departement',
            'class': 'form-control'
        }
    ))
