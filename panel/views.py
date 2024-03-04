from django.shortcuts import render
from products.models import product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Create your views here.
def home_panel_view(request):
    return render(request, template_name="panel/index.html")

def products_panel_view(request):
    model = product.objects.all()
    context = {
        "products":model
    }
    return render(request, template_name="panel/products.html", context=context)

def modify_product_view(request,pk):
    return HttpResponse(f"Product {pk} Delete")