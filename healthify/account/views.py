from django.shortcuts import render,redirect
from .forms import RegisterForm,PersonalInfoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import PersonalInfo,Appointment
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.contrib import messages
import datetime
from .middleware.appointment import appoinment_middleware
from django.contrib.auth.decorators import login_required
# Create your views here.
def registerView(request):
    form = RegisterForm() #blank form
    if request.method == 'POST':
        form = RegisterForm(request.POST) # filled form
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            name = form.cleaned_data['first_name']
            password = form.cleaned_data['password2']
            lname = form.cleaned_data['last_name']
            form.save()
            message = 'hey '+  str(name) +' '+ str(lname)+' Your registration has successfully completed. \n Your username :-  ' + str(
                username) + '  \n password:-' + str(password) + '\n thank you!, team Healthify.'
            subject = 'Thanks for joining with Healthify !!'
            send_mail(
                subject,
                message,
                'rahulvethekar95@gmail.com',
                [email],
                fail_silently=False,

            )
            return redirect('personal')

    template_name = 'account/register.html'
    context = {'form':form}
    return render(request,template_name,context)

def loginView(request):

    return_url = None
    return_url = request.GET.get('return_url')
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pwd')
        user1 = authenticate(username = u,password = p)
        if user1 is not None:
            login(request, user1)
            request.session['customer'] = user1.id #session created

            if return_url:
                return HttpResponseRedirect(return_url)
            else:
                #return_url = None
                return redirect('home')
        else:
            messages.error(request,'Invalid credentials!')

    template_name = 'account/login.html'
    return render(request,template_name)


def logoutView(request):
    logout(request)
    return redirect('login')


def personalView(request):

    request.session['customer'] = request.user.id
    customer=request.session.get('customer')
    print('customer',customer)
    if PersonalInfo.objects.filter(Select_Your_User_Id=customer).exists():
        return redirect('home')

    form = PersonalInfoForm()
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'account/personal.html'
    context = {'form':form}
    return render(request,template_name,context)


def personalInfoData(request):
    obj = PersonalInfo.objects.all()
    context = {'data':obj}
    template_name = 'admin/registerUser.html'
    return render(request,template_name,context)


def updateView(request,uid):
    obj = PersonalInfo.objects.get(id=uid)
    form = PersonalInfoForm(instance = obj)
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect('registerUsers')

    template_name = 'account/personal.html'
    context = {'form':form}
    return render(request,template_name,context)


def deleteView(request,did):
    obj = User.objects.get(id = did)
    obj.delete()
    return redirect('registerUsers')


@appoinment_middleware
def appointmentView(request):
    try:
        id = request.session.get('customer')
        print(id)
        data = PersonalInfo.objects.get(Select_Your_User_Id=id)
        d1 = request.GET.get('date')

        d = datetime.datetime.now()
        day = d.strftime("%d")
        month = d.strftime("%m")
        year = d.strftime("%Y")
        Date = str(day) + '/' + str(month) + '/' + str(year)


        if request.method == 'POST':
            uid = request.POST.get('userid')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            pincode = request.POST.get('pincode')
            blood_group = request.POST.get('blood_group')
            date = request.POST.get('date')
            time = request.POST.get('time')
            disease = request.POST.get('disease')
            vaccine = request.POST.getlist('vaccine')
            Day = str(date[0]) + str(date[1])
            Month = str(date[3]) + str(date[4])
            Year = str(date[6]) + str(date[7]) + str(date[8]) + str(date[9])
            if not int(Year) >= int(year) :
                messages.error(request,'Please select Valid year!')
                print('h1')
                return redirect('appointments')

            if  int(Year) == int(year) and  int(Month) < int(month):
                messages.error(request,'Please select Valid month!')
                print('h2')

                return redirect('appointments')


            if  int(Year) == int(year) and  int(Month) == int(month) and int(Day) < int(day):
                messages.error(request,'Please select Valid day!')
                print('h3')

                return redirect('appointments')



            obj = Appointment(uid = uid,first_name = fname , last_name = lname,gender = gender , age = age,email = email,mobile =mobile, address = address,pincode = pincode,blood_group = blood_group,date = date,time = time, Disease = disease,vaccine = vaccine  )
            obj.save()
            return redirect('appointments')
        x = Appointment.objects.filter(time='9AM to 12PM').aggregate(Count('time'))
        a = x.get('time__count')
        print('slotA', a)
        slotA = 2 - a

        y = Appointment.objects.filter(time='12PM to 2PM').aggregate(Count('time'))
        b = y.get('time__count')
        slotB = 2 - b

        p = Appointment.objects.filter(time='4PM to 6PM').aggregate(Count('time'))
        e = p.get('time__count')
        slotC = 2 - e

        z = Appointment.objects.filter(time='6PM to 8PM').aggregate(Count('time'))
        d = z.get('time__count')
        slotD = 2 - d

        all=a+b+e+d

        template_name = 'account/appointment.html'
        context = {'data':data,'a':a, 'b':b,'e':e,'d':d,'all':all,'slotA':slotA,'slotB':slotB,'slotC':slotC,'slotD':slotD,'date':Date}
        return render(request,template_name,context)
    except Exception as e:
        print(e)
        return redirect('personal')

def appointmentRequests(request):
    obj = Appointment.objects.all()
    context = {'data':obj}
    template_name = 'account/appointment_request.html'
    return render(request,template_name,context)


def appointmentDeleteView(request,did):
    obj = Appointment.objects.get(id = did)
    obj.delete()
    return redirect('appoint_requests')


def userProfileView(request):
    obj = PersonalInfo.objects.filter(Select_Your_User_Id = request.session.get('customer'))
    context = {'data':obj}
    template_name = 'account/profileview.html'
    return render(request,template_name,context)

