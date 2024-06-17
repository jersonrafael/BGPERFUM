from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from products.forms import *

from products.models import *
from orders.models import *
from categorys.models import *

"""

CATEGORYS VIEWS 

ALL VIEWS RELATED WITH THE CATEGORYS

"""
@login_required
# VIEW ALL CATEGORYS
def categorys_panel_view(request):
    model = category.objects.all()
    context = {
        "categorys":model,
    }
    return render(request, template_name="panel/categorys/categorys.html", context=context)

@login_required
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

@login_required
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

@login_required
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

@login_required
#DELETE CATEGORY
def delete_category_panel_view(request,pk):
    model = get_object_or_404(category, pk=pk)
    model.delete()
    return redirect(categorys_panel_view)