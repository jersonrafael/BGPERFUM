from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from products.forms import *

from products.models import *
from orders.models import *

import os

# VIEW TO SEE ALL PRODUCTS
@login_required
def products_panel_view(request):
    model = product.objects.all().order_by('-added_date')
    count_products = product.objects.count()
    paginator = Paginator(model, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "products":model,
        "page_obj": page_obj,
        'number_of_products':count_products
    }
    return render(request, template_name="panel/products/products.html", context=context)

# VIEW TO SEE ONE PRODUCT WITH MORE DETAILS
@login_required
def product_panel_view(request,pk):
    model = get_object_or_404(product,pk=pk)
    form = Product_form(instance=model)
    context = {
        'product':model,
        'form':form
    }
    return render(request, template_name="panel/products/product_panel.html", context=context)

# VIEW TO CREATE A PRODUCT
@login_required
def create_product_view(request):
    form = Product_form()

    context = {
        "form":form,
        'message':'',
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
@login_required
def modify_product_view(request,pk):
    model = get_object_or_404(product,pk=pk)
    form = Product_form(instance=model)
    if request.method == "POST":
        form = Product_form(request.POST, request.FILES,instance=model)
        if form.is_valid():
            form.save()
            return redirect(products_panel_view)
        else:
            return redirect(products_panel_view) 
    else:
        return redirect(products_panel_view)

# VIEW TO DELETE A PRODUCT
@login_required
def delete_product_view(request,pk):
    model = get_object_or_404(product,pk=pk)
    model.image.delete()
    model.delete()
    return redirect(products_panel_view)