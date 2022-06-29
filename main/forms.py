from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
#  maine inheitace from fors.Form)
class NewUserForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # add all fields including

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']  # cleaned_data - is created after is_valid() command
        if commit:
            user.save()
        return user

class BioForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['bio']