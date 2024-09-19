# templatetags/custom_filters.py
from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(name='alert_className')
def alert_className(value):
    if value == 0:
        return 'alert alert-warning'
    elif value == 1:
        return 'alert alert-success'
    elif value == 2:
        return 'alert alert-info'
    return ''

@register.simple_tag
def show_breadcrumb(folder=None):
    breadcrumb_html = ''
    
    # Start with the root node
    root_url = reverse('uploader:show_root_folder')
    breadcrumb_html += f"""
        <li class="breadcrumb-item">
            <a href="{root_url}">Root</a>
        </li>
    """
    
    # Iterate through parent folders
    current_folder = folder
    while current_folder:
        url = reverse('uploader:show_folder', args=[current_folder.id])
        name = current_folder.name
        breadcrumb_html = f"""
            <li class="breadcrumb-item">
                <a href="{url}">{name}</a>
            </li>
        """ + breadcrumb_html
        current_folder = current_folder.parent
    
    return mark_safe(f"""
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            {breadcrumb_html}
        </ol>
    </nav>
    """)