from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages

def homepage(request):
    messages.add_message(request, messages.info, "User logged in")
    return render(
        request,
        template_name="base.html",
        context=()
    )

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            homepage(request)
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
