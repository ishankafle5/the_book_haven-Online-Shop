from django import template

register = template.Library()


@register.filter
def first_item(items):
    return items[0].cart.total
