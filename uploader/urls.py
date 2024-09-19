from django.urls import path, include
from .views import show_folder
app_name = 'uploader'

urlpatterns = [
    # path('', index, name='index'),
    path('', show_folder, name='index'),
    path('folder/', show_folder, name='show_root_folder'),
    path('folder/<int:folder_id>', show_folder, name='show_folder')
]
