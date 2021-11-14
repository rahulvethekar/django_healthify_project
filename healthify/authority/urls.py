from django.urls import path
from .views import *

urlpatterns = [

    path('auth/',adminView,name = 'admin'),
    path('adminreg/', adminRegisterView ,name = 'adminRegister'),
    # -------------------- doctor ----------------------------------#

    path('doctor/', doctorView ,name = 'doctor'),
    path('doctor_list/', doctorRetriveView ,name = 'doctor_list'),
    path('doctor_update/<int:uid>/', doctorUpdate ,name = 'updateDoctor'),
    path('doctor_delete/<int:did>/', deleteDoctor ,name = 'deleteDoctor'),
    #-------------------- Nurse ----------------------------------#
    path('nurse/', nurseView, name='nurse'),
    path('nurse_list/', nurseRetriveView, name='nurse_list'),
    path('nurse_update/<int:uid>/', nurseUpdate, name='updateNurse'),
    path('nurse_delete/<int:did>/', deleteNurse, name='deleteNurse'),

]