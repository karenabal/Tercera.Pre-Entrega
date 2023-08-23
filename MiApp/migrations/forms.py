from django import forms
from .models import Clase1, Clase2, Clase3

class Clase1Form(forms.ModelForm):
    class Meta:
        model = Clase1
        fields = '_all_'

class Clase2Form(forms.ModelForm):
    class Meta:
        model = Clase2
        fields = '_all_'

class Clase3Form(forms.ModelForm):
    class Meta:
        model = Clase3
        fields = '_all_'