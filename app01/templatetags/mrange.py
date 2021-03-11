from django import template

register = template.Library()


@register.filter(name='mrange')
def mrange(number):
    return range(0, number)
