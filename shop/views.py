from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    perfums = product.objects.all()[:4]
    context = {
        'perfums': perfums
    }
    return render(request, template_name='shop/index.html', context=context)


def products(request):
    category_model = category.objects.all()
    products_model = product.objects.all()
    context = {
        'categorys': category_model,
        'products': products_model
    }
    if request.method == 'POST':
        category_id = request.POST
        print(category_id)
        return redirect(f'products/{category_id}')
    return render(request, template_name='shop/products.html', context=context)


def filter_product(request, pk):
    product_model = get_object_or_404(product, pk=pk)
    recomended = product.objects.order_by('?')[:5]
    # related_products = product.objects.get(category__contains=f'')
    context = {
        'product': product_model,
        'recomended':recomended
    }
    return render(request, template_name='shop/product.html', context=context)


def category_products(request, pk):
    products_model = product.objects.filter(category=pk)
    categorys_model = category.objects.all()
    context = {
        'categorys': categorys_model,
        'products': products_model
    }
    return render(request, template_name='shop/filter_products.html', context=context)


def search_product(request):
    data = request.POST["search"]
    products_model = product.objects.filter(name__contains=data)
    categorys_model = category.objects.all()
    context = {
        'categorys': categorys_model,
        'products': products_model
    }
    return render(request, template_name='shop/filter_products.html', context=context)

def category_view(request,pk):
    products_model = product.objects.filter(category_id=pk)
    category_model = category.objects.filter(id=pk)
    categorys_model = category.objects.all()
    context = {
        'categorys':categorys_model,
        'products':products_model
    }
    return render(request, template_name='shop/filter_products.html', context=context)
