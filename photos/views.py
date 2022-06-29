from django.shortcuts import render
from .forms import PhotosForm

def form_list(request):
    form = PhotosForm()
    return render(
        request=request,
        template_name="photos/list.html",
        context={'form': form}
    )