from django import template
register = template.Library()

@register.simple_tag
def define(val=None):
  print(type(val))
  return val