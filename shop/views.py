from django.shortcuts import render
from products.models import *

# Create your views here.
def home(request):
    perfums = product.objects.all()[:4]
    context = {
        'perfums':perfums
    }
    return render(request, template_name='shop/index.html', context=context)