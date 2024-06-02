from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from products.forms import *

from products.models import *
from orders.models import *

# Create your views here.
@login_required
def home_panel_view(request):
    recent_sales = sale.objects.order_by('-date')
    recent_added_products = product.objects.order_by('-added_date')
    user = request.user
    context = {
        'sales':recent_sales,
        'products':recent_added_products,
        'user':user
    }
    return render(request, template_name="panel/index.html", context=context)
