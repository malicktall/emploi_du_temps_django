from django import forms
from myApp.models import User


class EnseignantForm (forms.ModelForm, forms.Form):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_enseignant')

    username = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom de l\'enseignant',
            'class': 'form-control'
        }
    ))
    email = forms.EmailField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Email de l\'enseignant',
            'class': 'form-control'
        }
    ))
    password = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    

    is_enseignant = forms.BooleanField(required=False)
    


class RowEnseignantForm(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom de l\'enseignant',
            'class': 'form-control'
        }
    ))
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Email de l\'enseignant',
            'class': 'form-control'
        }
    ))

    password = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    
    is_enseignant = forms.BooleanField(required=False)
