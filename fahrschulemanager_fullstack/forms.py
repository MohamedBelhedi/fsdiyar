from django.forms import DateInput, TextInput
from .models import Prüflinge, Events
from django import forms

class AnmeldeForms(forms.ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
        widgets = {
            "date": DateInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d'),
            "text_event": TextInput(attrs={'class': 'text-event'}),
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
