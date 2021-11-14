from django.urls import path
from .views import *


urlpatterns = [
    path('login',loginView,name='login'),
    path('register', registerView, name='register'),
    path('logout', logoutView, name='logout'),
    path('personal',personalView,name = 'personal'),
    path('registerUsers',personalInfoData,name = 'registerUsers'),
    path('updateUser/<int:uid>/',updateView,name = 'updateUser'),
    path('deleteUser/<int:did>/',deleteView,name = 'deleteUser'),
    path('appointments',appointmentView,name = 'appointments'),
    path('appoint_request/',appointmentRequests,name = 'appoint_requests'),
    path('appointment_delete/<int:did>/',appointmentDeleteView,name = 'appoint_delete'),
    path('userprofile',userProfileView,name = 'userprofile'),


]