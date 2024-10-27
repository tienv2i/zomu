from django.shortcuts import render, get_object_or_404
from filer.models import File, Folder
from .forms import FileUploadForm
from django.http import HttpResponseNotFound

def show_folder(request, folder_id=None):
    
    folder = None if folder_id == None else get_object_or_404(Folder, id=folder_id)
    
    if folder is None:
        subfolders = Folder.objects.filter(parent__isnull=True).exclude(name="Private").order_by('name')
    else:
        # if folder.name == "Private":
        #     return HttpResponseNotFound("not found")
        subfolders = Folder.objects.filter(parent=folder).exclude(name="Private").order_by('name')
        
    files = File.objects.filter(folder=folder).order_by('name')
    
    context = {
        'current_folder': folder,
        'files': files,
        'subfolders': subfolders,
        'is_root_folder': folder_id==None
    }
    
    return render(request, 'uploader/show_folder.html', context)