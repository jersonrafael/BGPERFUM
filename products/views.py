from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator


from products.forms import *

from products.models import *
from orders.models import *

# VIEW TO SEE ALL PRODUCTS

def products_panel_view(request):
    model = product.objects.all().order_by('-added_date')
    paginator = Paginator(model, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "products":model,
        "page_obj": page_obj
    }
    return render(request, template_name="panel/products/products.html", context=context)

# VIEW TO SEE ONE PRODUCT WITH MORE DETAILS

def product_panel_view(request,pk):
    model = get_object_or_404(product,pk=pk)
    form = Product_form(instance=model)
    context = {
        'product':model,
        'form':form
    }
    return render(request, template_name="panel/products/product_panel.html", context=context)

# VIEW TO CREATE A PRODUCT

def create_product_view(request):
    form = Product_form()
    context = {
        "form":form,
        'message':''
}

    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            if product.objects.filter(name=form.cleaned_data.get('name')):
                context['message'] = 'Ya existe un producto con ese nombre'
                return render(request,template_name="panel/products/create_product.html", context=context)                

            form.save() 
            return redirect(products_panel_view)
        else:
            return render(request,template_name="panel/products/create_product.html", context=context)
    else:
        form = Product_form()
    return render(request,template_name="panel/products/create_product.html", context=context)

# VIEW TO MODIFY A PRODUCT

def modify_product_view(request,pk):
    model = get_object_or_404(product,pk=pk)
    form = Product_form(request.POST, request.FILES, instance=model)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(products_panel_view)
        else:
            return redirect(products_panel_view) 
    else:
        return redirect(products_panel_view)

# VIEW TO DELETE A PRODUCT

def delete_product_view(request,pk):
    model = get_object_or_404(product,pk=pk)
    context ={
        "Delete":"Estas seguro que deseas eliminar el producto?",
        "product":model
    }
    if request.method == "GET":
        return render(request, template_name="panel/products/delete_product.html",context=context)
    elif request.method == "POST":
        model = get_object_or_404(product, pk=pk)
        model.delete()
        return redirect(products_panel_view)



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
    return render(request, template_name="panel/categorys/categorys.html", context=context)


def category_panel_view(request,pk):
    model = get_object_or_404(category, pk=pk)
    form = Category_form(instance=model)
    context = {
        'form': form,
        'category':model,
        'message':''
    }

    if request.method =='POST':
        form = Category_form(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect(categorys_panel_view)
        else:
            context['message'] = 'Error al actulizar la categoria revisa que todo este correcto'
            return render(request, template_name='panel/categorys/category.html',context=context)

    else:
        return render(request, template_name='panel/categorys/category.html',context=context)

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
            return redirect(categorys_panel_view)
        else:
            return redirect(categorys_panel_view)
    else:
        form = Category_form()
    return render(request, template_name='panel/categorys/create_category.html',context=context)

# EDIT CATEGORY

def edit_category_view(request,pk):
    model = get_object_or_404(category,pk=pk)
    form = Category_form(request.POST, request.FILES, instance=model)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(categorys_panel_view)
        else:
            return redirect(categorys_panel_view) 
    else:
        return redirect(categorys_panel_view)

#DELETE CATEGORY
def delete_category_panel_view(request,pk):
    model = get_object_or_404(category, pk=pk)
    form = Category_form(instance=model)
    context = {
        'form':form,
        'category':model,
        'message':''
    }

    if request.method == 'POST':
        model.delete()
        return redirect(categorys_panel_view)
    return render(request, template_name='panel/categorys/category.html', context=context)