from django import template

register = template.Library()


@register.filter
def first_item(items):
    return items[0].cart.total


@register.filter
def card_Iid(items):
    return items[0].cart.id


@register.filter
def return5items(items):
    return items[0:5]


@register.filter
def categorytype(items):
    return items[0].category
