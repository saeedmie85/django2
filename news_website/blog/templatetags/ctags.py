import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_time(strformat):
    return datetime.datetime.now().strftime(strformat)
