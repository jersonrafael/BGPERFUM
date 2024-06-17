from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from products.forms import *

from products.models import *
from orders.models import *
from django.db.models import Sum

# Create your views here.

"""

VIEWS TO MANAGE THE SELS OR ORDERS

"""
@login_required
def orders_panel_view(request):
    recent_sales = sale.objects.order_by('-date')
<<<<<<< HEAD
    total_of_sales = sale.objects.count()
=======
    total_of_sales = sale.objects.all().aggregate(total_sales=Sum('total'))['total_sales']
>>>>>>> routes
    context = {
        "sales":recent_sales,
        'total_of_sales':total_of_sales
    }
    return render(request, template_name="panel/sales/sales_panel.html", context=context)

@login_required
def order_panel_view(request,pk):
    model = get_object_or_404(sale, pk=pk)
    form = sale_form(instance=model)
    context = {
        'sale':model,
        'form':form,
        'message':''
    }
    if request.method == 'POST':
        form = sale_form(request.POST, instance=model)
        if form.is_valid():
            product_name = form.cleaned_data.get("product")
            quantity = form.cleaned_data.get("quantity")
            get_product = product.objects.get(name=product_name)
            if get_product.stock <= 0:
                context['message'] = 'Este producto tiene 0 unidades disponibles'
                # return render(request, template_name='panel/sales/create_sale.html',context=context)
            elif quantity > get_product.stock:
                print(context)
                context['message']= f'Este producto tiene menos de {quantity} unidades disponibles'
                # return render(request, template_name='panel/sales/create_sale.html',context=context)
            else:
                # Restar la cantidad del stock y guardar el producto
                get_product.stock -= quantity
                get_product.save()
                # Guardar la venta
                form.save()
                return redirect(orders_panel_view)
    return render(request, template_name='panel/sales/sale.html',context=context)

@login_required
def create_order_panel_view(request):
    form = sale_form()
    context= {
        'form':form,
        'message':''
    }

    if request.method == 'POST':
        form = sale_form(request.POST)
        if form.is_valid():
            print('Form valido')
            product_name = form.cleaned_data.get("product")
            quantity = form.cleaned_data.get("quantity")
            get_product = product.objects.get(name=product_name)
            if get_product.stock <= 0:
                print('No hay')
                context['message'] = 'Este producto tiene 0 unidades disponibles'
                return render(request, template_name='panel/sales/create_sale.html',context=context)
            elif quantity > get_product.stock:
                print('Error stock')
                context['message']= f'Este producto tiene menos de {quantity} unidades disponibles'
                return render(request, template_name='panel/sales/create_sale.html',context=context)
            else:
                print('Exito')
                # Restar la cantidad del stock y guardar el producto
                get_product.stock -= quantity
                get_product.save()
                form.save()
                # Guardar la venta
                return redirect(orders_panel_view)
        else:
            print('Form invalido')

    return render(request, template_name='panel/sales/create_sale.html',context=context)

@login_required
def delete_order_panel_view(request,pk):
    model = get_object_or_404(sale, pk=pk)
    model.delete()
    return redirect(orders_panel_view)
