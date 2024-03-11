from django.forms import ModelForm
from django import forms
from products.models import *


class Category_form(forms.Form):
    name = forms.CharField(label="Nombre de la Categoria",error_messages={'required':'No dejes el campo vacio'}, widget=forms.TextInput(attrs={'class':'text-blue-600','autocomplete':'off'}))

class Product_form(forms.Form):
    image= forms.CharField(label="Imagen del Producto",widget=forms.FileInput)
    name = forms.CharField(label="Nombre del Producto")
    description = forms.CharField(label="Descripcion del Producto",widget=forms.Textarea)
    price = forms.IntegerField(label="Precio del Producto")
