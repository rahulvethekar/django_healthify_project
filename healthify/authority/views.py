from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import AdminRegisterForm
from .forms import DoctorModelForm,NurseModelForm,RoomService
from .models import Doctor,Nurse,RoomService
# Create your views here.
def adminView(request):
    if request.user.is_superuser == True:
        template_name = 'admin/home.html'
        return render(request,template_name)
    else:
        print('admin login only!')
        messages.error(request,'Admin access only!!')
        return redirect('login')
def adminRegisterView(request):
    form = AdminRegisterForm()
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')

    template_name = 'admin/adminRegister.html'
    context = {'form':form}
    return render(request,template_name,context)

########################### Doctor's##########################

def doctorView(request):
    form = DoctorModelForm()
    if request.method == 'POST':
        form = DoctorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    template_name = 'admin/doctor.html'
    context = {'form':form}
    return render(request,template_name,context)


def doctorRetriveView(request):
    obj = Doctor.objects.all()
    context= {'data':obj}
    template_name = 'admin/doctor_list.html'
    return render(request,template_name,context)


def doctorUpdate(request,uid):
    obj = Doctor.objects.get(id = uid)
    form = DoctorModelForm(instance = obj)
    if request.method == 'POST':
        form = DoctorModelForm(request.POST,instance = obj)
        form.save()
        return redirect('doctor_list')
    template_name = 'admin/Doctor.html'
    context = {'form':form}
    return render(request,template_name,context)

def deleteDoctor(request,did):
    obj = Doctor.objects.get(id = did)
    obj.delete()
    return redirect('doctor_list')

#########################  Nurse   ##################

def nurseView(request):
    form = NurseModelForm
    if request.method == 'POST':
        form = NurseModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    template_name = 'admin/Nurse.html'
    context = {'form':form}
    return render(request,template_name,context)


def nurseRetriveView(request):
    obj = Nurse.objects.all()
    context= {'data':obj}
    template_name = 'admin/nurse_list.html'
    return render(request,template_name,context)


def nurseUpdate(request,uid):
    obj = Nurse.objects.get(id = uid)
    form = NurseModelForm(instance = obj)
    if request.method == 'POST':
        form = NurseModelForm(request.POST,instance = obj)
        form.save()
        return redirect('nurse_list')
    template_name = 'admin/Nurse.html'
    context = {'form':form}
    return render(request,template_name,context)

def deleteNurse(request,did):
    obj = Nurse.objects.get(id = did)
    obj.delete()
    return redirect('nurse_list')

#########################  Room Service   ##################

