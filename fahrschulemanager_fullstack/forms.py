from django.forms import DateInput, TextInput
from .models import Prüflinge, Events
from django import forms



class AnmeldeForms(forms.ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
        widgets = {
            "date": DateInput(attrs={'class': 'datepicker'}, format='%d.%m.%Y'),
            "text_event": TextInput(attrs={'class': 'text-event'}),
        }


class Pruefung(forms.ModelForm):
    class Meta:
        model = Prüflinge
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "bezahlt": forms.TextInput(attrs={'class': 'form-control'}),
            "prüfungsdatum": forms.DateInput(format='%d.%m.%Y')
        }
