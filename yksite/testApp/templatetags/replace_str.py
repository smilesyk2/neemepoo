from django import template

register = template.Library()

@register.filter(name='replace_str')
def replace_str(str):
    return str.replace('<!HS>', '<span class="strong">').replace('<!HE>', '</span>')