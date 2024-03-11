from django.shortcuts import render
from products.models import product,category
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from products.forms import *


# Create your views here.
def home_panel_view(request):
    return render(request, template_name="panel/index.html")

"""

PRODUCTS VIEWS 

ALL VIEWS RELATED WITH THE PRODUCTS

"""

def products_panel_view(request):
    model = product.objects.all()
    context = {
        "products":model
    }
    return render(request, template_name="panel/products.html", context=context)

def create_product_view(request):
    form = Product_form()
    context = {
        "form":form
    }

    if request.method == 'POST':
        if form.is_valid():
            form = Product_form(request.POST)
            form.save()
            return HttpResponse("Saved") 
    return render(request,template_name="panel/create_product.html", context=context)

def modify_product_view(request,pk):
    return HttpResponse(f"Product {pk} Delete")

"""

CATEGORYS VIEWS 

ALL VIEWS RELATED WITH THE CATEGORYS

"""

# VIEW ALL CATEGORYS
def categorys_panel_view(request):
    model = category.objects.all()
    context = {
        "categorys":model,
    }
    return render(request, template_name="panel/categorys.html", context=context)

# CREATE CATEGORY 
def create_category_view(request):
    form = Category_form(request.POST)
    context = {
        'form': form
    }

    if request.method =='POST':
        if form.is_valid():
            model = category.objects.create(name=request.POST["name"])
            model.save()
            return HttpResponse("Valid")
        else:
            return HttpResponse("Not Valid")
    else:
        form = Category_form()
    return render(request, template_name='panel/create_category.html',context=context)