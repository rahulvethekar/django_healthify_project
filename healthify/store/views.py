from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from .models import Product,Order,Payment
from .filters import ProductFilter
from django.views import View
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from .middleware.auth import auth_middleware
from django.db.models import Sum
from .templatetags.cart import final_total
import razorpay
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.paginator import Paginator,Page,PageNotAnInteger,EmptyPage,InvalidPage
import time
KEY_ID = 'rzp_test_TLv6UYKwn2iZHL'
KEY_SECRET = 'JSbqCKTGXXvT3SvmojJubYU8'

# Create your views here.
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

class HomeView(TemplateView):

    template_name = 'store/home.html'


class HealthcareView(View):

    def get(self,request):
        cart= request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        item = request.GET.get('items')
        if item != '' and item is not None:
            obj = Product.objects.filter(Name__icontains=item)
        else:
            obj = Product.objects.all()

        filter1 = ProductFilter(request.GET , queryset = obj)
        context = {'filter1':filter1}

        paginator = Paginator(filter1.qs,4,orphans=3)  # filled object to paginator
        page_number = request.GET.get('page')  # dynamically page number from url


        page_obj = paginator.get_page(page_number)  # specific page number passed to template

        context = {'page_obj':page_obj}


        template_name = 'store/healthcare.html'
        return render(request,template_name,context={ 'filter1':filter1,'page_obj':page_obj })

    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity -1
                else:
                    cart[product]= quantity + 1 #appends
                    print(cart)
            else:
                cart[product] =  1
        else:
            cart = {}
            cart[product]=1   #appends
        print('type',type(cart))
        request.session['cart'] = cart
        print(request.session['cart'])

        return redirect('store_healthcare')


class CartView(View):

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        products =Product.objects.filter(id__in=ids)
        context = {'data':products}
        template_name = 'store/cart.html'
        return render(request,template_name,context)



class CheckoutView(View):
    def post(self,request):
        address = request.POST.get('address')
        mobile = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        products = Product.objects.filter(id__in=ids)
        print(address,mobile,customer,cart,products,)
        request.session['token'] = randint(1246,3245)
        token = request.session.get('token')
        for product in products:

            order = Order(
                            Customer = User( id = customer),
                            Product = product,
                            Price = product.Price,
                            Address = address,
                            Mobile = mobile,
                            Quantity = cart.get(str(product.id)),
                            payment_token = token
                )
            order.save()
        print(token)
        return redirect('payment')


class PaymentView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('login')

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        products = Product.objects.filter(id__in=ids)
        price = final_total(products, cart) * 100

        user = request.user
        action = request.GET.get('action')
        order = None
        payment = None
        if action == 'create_payment':

            amount=int(price)
            currency = 'INR'
            notes = {'email' : user.email,'name': f'{user.first_name}  {user.last_name}'}

            receipt = f'healthify:  {int(randint(10000,40000))}'

            order = client.order.create({'amount':amount,'currency':currency,'notes':notes,'receipt':receipt})
            payment = Payment()
            payment.user = user
            payment.price = price/100
            payment.order_id = order.get('id')
            print('order id:',order.get('id'))

            payment.save()


        context = {'data': products,'order':order,'payment':payment}
        template_name = 'store/payment.html'
        return render(request, template_name, context)

class OrderView(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.objects.filter(Customer = customer).order_by('-date')
        context = {'orders':orders}
        template_name = 'store/order.html'
        return render(request,template_name,context)

@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        print(data)

        try:
            client.utility.verify_payment_signature(data)
            payment_id = data.get('razorpay_payment_id')
            order_id = data.get('razorpay_order_id')

            if payment_id:

                obj1 = Payment.objects.get(order_id= order_id)
                obj1.payment_id = payment_id
                obj1.save()

                key = request.session.get('token')
                print(key)

                obj= Order.objects.filter(payment_token = key).update(payment_status='True')


            request.session['cart'] = {}
            request.session['payment_token'] = {}
            return redirect('payment_success')
        except Exception as e:
            print(e)
            return redirect('order')


class PaymentSucess(TemplateView):
    template_name = 'store/paymentsuccessfull.html'



