from django import template


def full(value):
    if value == 'in':
        return 'Internship'
    elif value == 'ft':
        return 'Full-Time'
    elif value == 'pt':
        return 'Part-Time'
    else:
        return 'Unknown'

register = template.Library()
register.filter('full', full)
