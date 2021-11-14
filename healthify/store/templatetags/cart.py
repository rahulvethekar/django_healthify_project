from django import template
register = template.Library()


@register.filter(name = 'is_in_cart')     # to check product is in cart or not
def is_in_cart(prods,cart):
    keys = cart.keys()
    for id in keys:

        if int(id) == prods.id:
            return True

    return False


@register.filter(name = 'cart_quantity')    #product quantity in cart
def cart_quantity(prods,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == prods.id:
            return cart.get(id)

    return False

@register.filter(name = 'cart_total')  #final price of all quantity
def cart_total(prods,cart):
    return prods.Price * cart_quantity(prods,cart)

@register.filter(name = 'final_total') #grand total of price
def final_total(prods,cart):
    sum = 0
    for i in prods:
        sum += cart_total(i,   cart)
    return sum


@register.filter(name = 'purchase_total')
def purchase_total(cart):                   #product quantity in cart
    sum = 0
    if not cart:
      sum = 0
      return sum

    else:
        value = cart.values()
        for list in value:
            sum += list
        return sum


