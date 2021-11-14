from django import template
register = template.Library()

@register.filter(name = 'multiply')
def multiply(quantity,price):      #total price of all quantity
    return quantity * price


@register.filter(name = 'total')
def total(order):                  #Grand total of price
    sum = 0
    for p in order:
       sum+= multiply(p.Quantity,p.Price)

    return sum