from django import template

register = template.Library()

@register.filter(name='make_range')
def make_range(count):
    return range(int(count))