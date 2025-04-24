# dashboard/templatetags/nav_extras.py

from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active_link(context, pattern):
    request = context.get('request')
    if request and request.path.startswith(pattern):
        return 'active'
    return ''
