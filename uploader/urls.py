from django.urls import path, include
from .views import index
app_name = 'uploader'

urlpatterns = [
    path('', index, name='index')
]
