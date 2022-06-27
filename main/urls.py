from django.urls import path
from .views import register_request

app_name = 'main'
urlpatterns = [
    path('', register_request, name='register'),
]