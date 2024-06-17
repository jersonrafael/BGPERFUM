from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.
def login_view(request):
<<<<<<< HEAD
    pass

def register_view(request):
    pass

def logout_view(request):
    pass
=======
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/panel/")
        else:
            pass #error 
    return render(request,template_name="panel/auth_templates/login.html")

def register_view(request):
    return render(request,template_name="panel/auth_templates/register.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
>>>>>>> routes
