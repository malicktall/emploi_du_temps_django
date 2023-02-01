from django import forms
from myApp.models import Creneau
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class CreneauForm (forms.ModelForm, forms.Form):

    class Meta:
        model = Creneau
        fields = ('date', 'heureDebut', 'heureFin',
                  'enseignant', 'matiere', 'filiere', 'types',)
        widgets = {
            "date": AdminDateWidget(),
            "time": AdminTimeWidget(),
        }

    date = forms.DateField(label='', widget=AdminDateWidget())
    heureDebut = forms.TimeField()
    heureFin = forms.TimeInput()
    enseignant = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            # 'placeholder': 'Nom de la matière',
            'class': 'form-control'
        }
    ))
    matiere = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            # 'placeholder': 'Nom de la matière',
            'class': 'form-control'
        }
    ))
    filiere = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            # 'placeholder': 'Nom de la matière',
            'class': 'form-control'
        }
    ))
    types = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Example:Cours, TD / TP ',
            'class': 'form-control'
        }
    ))


class RowCreneauForm(forms.Form):
    date_input = forms.DateField(widget=AdminDateWidget(
        # attrs= {
        #     'class':'form-control'
        # }
    )
    )
    heureDebut = forms.TimeField()
    heureFin = forms.TimeInput()
    enseignant = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            # 'placeholder': 'Nom de la matière',
            'class': 'form-control'
        }
    ))
    matiere = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            # 'placeholder': 'Nom de la matière',
            'class': 'form-control'
        }
    ))
    filiere = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            # 'placeholder': 'Nom de la matière',
            'class': 'form-control'
        }
    ))
    types = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Example:Cours, TD / TP ',
            'class': 'form-control'
        }
    ))
