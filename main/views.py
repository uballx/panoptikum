from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages

def homepage(request):
    messages.add_message(request, messages.INFO, "Hello")
    return render(
        request,
        template_name="base.html",
        context={}
    )

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "User registered")
            messages.add_message(request, messages.INFO, "User logged in")
            return redirect("/")
    else:
        form = NewUserForm()

    context = {
        'form': form,
    }

    return render(
        request=request,
        template_name="main/register.html",
        context=context
    )

def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logged as {username}")
                return redirect("/")
            else:
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid username or password")

    form = AuthenticationForm()
    return render(
        request=request,
        template_name="main/login.html",
        context={'login_form': form}
    )

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out")
    return redirect("/")