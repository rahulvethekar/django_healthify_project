from django import template
register = template.Library()

@register.filter(name = 'currency')  #currency symbol to prices
def currency(number):
    return str('₹' )  + str(number)