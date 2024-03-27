from django.shortcuts import render, get_object_or_404
from products.models import *

# Create your views here.
def home(request):
    perfums = product.objects.all()[:4]
    context = {
        'perfums':perfums
    }
    return render(request, template_name='shop/index.html', context=context)

def products(request):
    categorys_model = category.objects.all()
    products_model = product.objects.all()
    context = {
      'categorys':categorys_model,
      'products':products_model
    }
    return render(request, template_name='shop/products.html', context=context)