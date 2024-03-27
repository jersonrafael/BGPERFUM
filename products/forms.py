from django.forms import ModelForm
from django import forms
from products.models import *
from orders.models import *


class Category_form(forms.ModelForm):
    class Meta:
        model= category
        fields = '__all__'
        labels = {
            'name':('Nombre de la categoria'),
            'avaliable':('Disponible')
        }

    # name = forms.CharField(label="Nombre de la Categoria",
    # error_messages={'required':'No dejes el campo vacio'}, 
    # widget=forms.TextInput(attrs={'class':'text-blue-600','autocomplete':'off'}))

class Product_form(forms.ModelForm):

    class Meta:
        model = product
        fields = ["image","name","description","price","stock","discount_code","avaliable","category"]
        labels = {
            'image': ("Imagen del Producto"),
            'name': ("Nombre"),
            'description': ("Descripcion del Producto"),
            'price':("Precio del Producto"),
            'stock':("Catidad disponible del Producto"),
            'diPscount_code':("Codigo de descuento (Opcional)"),
            'avaliable':("Si el producto esta o no disponible"),
            'category':("Categoria del producto")

        }
        widgets={
            'image': forms.FileInput(attrs={'class': 'image-input_form'}),
            'name': forms.TextInput(attrs={'class': 'name-input_form'}),
            'description': forms.Textarea(attrs={'class': 'description-input_form'}),
            'price': forms.TextInput(attrs={'class': 'price-input_form'}),
            'stock': forms.TextInput(attrs={'class': 'stock-input_form'}),
            'discount_code': forms.Select(attrs={'class': 'discount_code-input_form'}),
            'avaliable': forms.CheckboxInput(attrs={'class': 'avaliable-input_form'}),
            'category': forms.Select(attrs={'class': 'category-input_form'}),


        }
        error_messages = {
            'image': {
                'required': "El campo Imagen es requerido.",
            },
            'name': {
                'required': "El campo Nombre es requerido.",
            },
            'description': {
                'required': "El campo Descripción es requerido.",
            },
            'price': {
                'required': "El campo Precio es requerido.",
            },
            'stock': {
                'required': "El campo Stock es requerido.",
            },
            'discount_code': {
                'required': "El campo Código de descuento es requerido.",
            },
            'avaliable': {
                'required': "El campo Disponible es requerido.",
            },
            'category': {
                'required': "El campo Categoría es requerido.",
            },
        }
    # image= forms.FileField()
    # name = forms.CharField(label="Nombre del Producto")
    # description = forms.CharField(label="Descripcion del Producto",widget=forms.Textarea)
    # price = forms.IntegerField(label="Precio del Producto")

class sale_form(forms.ModelForm):
    class Meta:
        model = sale
        fields = '__all__'
        labels = {
            'product':('Nombre del producto'),
            'quantity':('Cantidad')
        }
        