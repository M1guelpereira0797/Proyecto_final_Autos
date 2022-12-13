from django import forms
from familia.models import familia

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100, 
widget=forms.TextInput(attrs={"placeholder": "Busque algo"}))
class familiaform(forms.ModelForm):
  class Meta:
    model = familia
    fields = ['nombre', 'direccion', 'numero_pasaporte']