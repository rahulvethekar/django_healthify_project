from django.urls import path
from .views import *


urlpatterns =[
    path('home',HomeView.as_view(),name = 'store_home'),
    path('healthcare',HealthcareView.as_view(),name = 'store_healthcare'),
    path('cart',CartView.as_view(),name = 'cart'),
    path('checkouts',CheckoutView.as_view(),name = 'checkout'),
    path('order',OrderView.as_view(),name = 'order'),
    path('payment',PaymentView.as_view(),name = 'payment'),
    path('verify_payment',verifyPayment,name = 'verify_payment'),
    path('payment_sucessfully',PaymentSucess.as_view(),name = 'payment_success'),


]