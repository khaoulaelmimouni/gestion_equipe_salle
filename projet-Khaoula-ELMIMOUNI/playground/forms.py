from django import forms
from .models import Equipe, salle

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['id_equipe', 'logo', 'situation', 'adversaire', 'lieu']

    widgets = {
        'situation': forms.Select(choices=[('interieur', 'Intérieur'), ('exterieur', 'Extérieur')]),
        'adversaire': forms.TextInput(attrs={'placeholder': 'Nom de l\'équipe adversaire'}),
    }

class salleForm(forms.ModelForm):
    class Meta:
        model = salle
        fields = ['id_salle', 'capacite', 'occupe', 'image']  