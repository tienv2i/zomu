from django import template
from uploader.utils import get_breadcrumb_list

register = template.Library()

@register.inclusion_tag('uploader/breadcrumb.html', takes_context=True)
def breadcrumb(context, folder=None):
    # Lấy danh sách breadcrumb từ hàm get_breadcrumb_list
    breadcrumb_list = get_breadcrumb_list(folder)
    return {
        'breadcrumb_list': breadcrumb_list
    }