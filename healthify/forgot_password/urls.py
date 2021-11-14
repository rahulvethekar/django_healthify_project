from django.urls import path
from .views import *

urlpatterns = [
    path('form/',forgotPassword,name='resetpass'),
    path('Changepassword/',changepassword,name='changepassword'),
    path('reset/',forgotDetailsView,name='resetpassword'),
]
