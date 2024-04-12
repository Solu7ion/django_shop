from django import template
register = template.Library()

@register.filter
def currency(value):
    return f"${value}"

@register.simple_tag
def copyright():
    return "&copy; 2024 Интернет-магазин"