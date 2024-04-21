#from django import forms

from django import forms
from django.core.exceptions import ValidationError

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

    # Validación personalizada para el campo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        
        # Verifica que el campo nombre solo contenga letras y espacios
        if not nombre.replace(' ', '').isalpha():
            raise ValidationError("El campo nombre solo puede contener letras y espacios.")
        
        return nombre
    
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
