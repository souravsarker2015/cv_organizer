from django import template

register = template.Library()


@register.filter(name='remove_special')
def remove_cars(value, args):
    print(value)
    print(args)
    for character in args:
        print(character)
        value = value.replace(character, "")
    return value
