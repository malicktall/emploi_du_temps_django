from django import forms
from myApp.models import Matiere

class MatiereForm (forms.ModelForm, forms.Form):
    
    class Meta:
        model = Matiere
        fields = ('name',)
    
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom de la matière',
            'class': 'form-control'
        }
    ))

class RowMatiereForm(forms.Form):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs= {
            'placeholder':'Nom de la matière',
            'class': 'form-control'
        }
    ))