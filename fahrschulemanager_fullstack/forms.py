from .models import Prüflinge, Events
from django import forms



class AnmeldeForms(forms.ModelForm):
    class Meta:
        model = Prüflinge
        fields = "__all__"

class Pruefung(forms.ModelForm):
    class Meta:
        model = Events
        fields = "__all__"      