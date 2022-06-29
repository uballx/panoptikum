from django.urls import path
from .views import form_list


app_name = 'photos'
urlpatterns = [
    path('photos/', form_list, name='form_list'),
]