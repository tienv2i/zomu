# forms.py
from django import forms
from filer.models import File

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'description']