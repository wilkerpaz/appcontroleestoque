from django.template import Library

register = Library()


@register.inclusion_tag('pagination.html')
def pagination(request, paginator, page_obj):
    context = {'paginator': paginator, 'page_obj': page_obj, 'request': request}
    return context
