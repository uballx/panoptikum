from django import forms
from .models import Galeria

class PhotosForm(forms.ModelForm):

    class Meta:
        model = Galeria
        fields = '__all__'