from django import template


register = template.Library()

CENSOR_WORDS = [
    '***',
    '****'
]

@register.filter()
def censor(value):

    for word in CENSOR_WORDS:
        value = value.replace(word, '*' * len(word))
    return value