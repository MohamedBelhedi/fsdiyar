from django.forms import DateInput, TextInput
from .models import Prüflinge, TüvTermine, PrüflingeTheorie
from django import forms

class AnmeldeForms(forms.ModelForm):
    class Meta:
        model = TüvTermine
        fields = "__all__"
        widgets = {
            "date": DateInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d'),
            "text_event": TextInput(attrs={'class': 'text-event'}),
        }

class TheorieForm(forms.ModelForm):
    class Meta:
        model = PrüflingeTheorie
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={'class': 'form-control'}),
            "vorname": TextInput(attrs={'class': 'form-control'}),
            "lernerfolg": TextInput(attrs={'class': 'form-control'}),
            "anrufdatum": DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d')

        }

class Pruefung(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(Pruefung, self).__init__(*args, **kwargs)
        if user:
            self.fields['fl'].initial = user.username

    class Meta:
        model = Prüflinge
        fields = "__all__"
        widgets = {
            "fl": forms.TextInput(attrs={'class': 'form-control'}),
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "bezahlt": forms.TextInput(attrs={'class': 'form-control'}),
            "prüfungsdatum": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d')
        }
