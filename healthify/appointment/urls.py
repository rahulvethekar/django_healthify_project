from django.urls import path
from .views import *

urlpatterns = [
    path('form/',appointmentView,name = 'appointment'),
    path('request/',appointmentRequestView,name = 'appoint_request')

]