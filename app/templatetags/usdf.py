from django import template

register=template.Library()


@register.filter(name='swapping')
def swap(value):
    return value.swapcase()
@register.filter()
def counting(value,arg):
    return value.count(arg)
@register.filter()
def removing(value,arg):
    return value.replace(arg,'')


#register.filter('swapping',swap)
#register.filter('counting',counting)
#register.filter('removing',removing)