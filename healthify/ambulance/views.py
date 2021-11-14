from django.shortcuts import render,redirect
from .models import Ambulance
from.forms import AmbulanceModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def ambulanceView(request):
    form = AmbulanceModelForm()
    if request.method == 'POST':
        form = AmbulanceModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booked')

    template_name = 'ambulance/ambulance.html'
    context = {'form':form}
    return render(request,template_name,context)

def ambulancerequestView(request):
    obj = Ambulance.objects.all()
    template_name = 'ambulance/ambulancerequest.html'
    context = {'data':obj}
    return render(request,template_name, context)

def deleteView(request,did):
    obj = Ambulance.objects.get(id=did)
    obj.delete()

    return redirect('request')

def bookedView(request):
    template_name = 'ambulance/booked.html'
    return render(request, template_name)