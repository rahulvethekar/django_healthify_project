from django.urls import path
from .views import *
urlpatterns = [
    path('a_call/',ambulanceView,name='ambulance'),
    path('ambu-request/', ambulancerequestView, name='request'),
    path('delete/<int:did>/', deleteView, name='delete_req'),
    path('booked/', bookedView, name='booked'),

]