from django.shortcuts import render,redirect
from .forms import AppointmentForm
from .models import Appointment
from functools import wraps
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = 'login')
def appointmentView(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    template_name = 'appointment/appointment.html'
    context = {'form':form}
    return render(request,template_name,context)

def appointmentRequestView(request):
    obj = Appointment.objects.all()
    context = {'data':obj}
    template_name = 'appointment/request.html'
    return render(request,template_name,context)



