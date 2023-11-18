from django import forms
from inicio.models import Zapatilla
from ckeditor.fields import RichTextFormField



class BaseZapatillaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    anio = forms.IntegerField()
    
    
class CrearZapatillaFormulario(BaseZapatillaFormulario):
    ...


class ActualizarZapatillaFormulario(BaseZapatillaFormulario):
    ...
    

class BusquedaZapatillaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    