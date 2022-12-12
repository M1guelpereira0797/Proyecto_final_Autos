from django import forms
from familia.models import familia

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = familia
    fields = ['nombre', 'direccion', 'numero_pasaporte']