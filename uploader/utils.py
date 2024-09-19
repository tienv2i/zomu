from django.urls import reverse

def get_breadcrumb_list(folder=None):
    breadcrumb_list = []

    # Thêm breadcrumb cho thư mục gốc (Root)
    breadcrumb_list.append({
        'url': reverse('uploader:show_root_folder'),
        'name': 'Root'
    })
    
    # Duyệt qua các thư mục cha
    current_folder = folder
    while current_folder:
        breadcrumb_list.insert(1, {
            'url': reverse('uploader:show_folder', args=[current_folder.id]),
            'name': current_folder.name
        })
        current_folder = current_folder.parent

    return breadcrumb_list