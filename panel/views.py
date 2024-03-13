from django.shortcuts import render
from products.models import product,category
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect

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

def product_panel_view(request,pk):
    model = get_object_or_404(product,pk=pk)
    form = Product_form(instance=model)
    context = {
        'product':model,
        'form':form
    }
    return render(request, template_name="panel/product_panel.html", context=context)

def create_product_view(request):
    form = Product_form(request.POST, request.FILES)
    context = {
        "form":form
    }

    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect("panel_products")
        else:
            return render(request,template_name="panel/create_product.html", context=context)
    else:
        form = Product_form()
    return render(request,template_name="panel/create_product.html", context=context)

def modify_product_view(request,pk):
    model = get_object_or_404(product,pk=pk)
    form = Product_form(request.POST, request.FILES, instance=model)
    if request.method == "POST":
        # data = request.POST
        # update = model.update(name=data["name"],description=data["description"],stock=data["stock"])
        # print(data)
        if form.is_valid():
            form.save()
            return redirect("panel_products")
        else:
            # return redirect("panel_products")
            return HttpResponse("Error")
    else:
        return redirect("panel_products")

def delete_product_view(request,pk):
    context ={
        "Delete":"Estas seguro que deseas eliminar el producto?"
    }
    if request.method == "GET":
        return render(request, template_name="delete_product.html",context=context)
    elif request.method == "POST":
        return HttpRedirect("panel/products")

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