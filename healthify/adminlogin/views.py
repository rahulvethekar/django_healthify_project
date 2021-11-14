from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AdminRegister
from django.contrib.auth.hashers import check_password,make_password
# Create your views here.

def adminRegisterView(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        decode = make_password(password)
        obj = AdminRegister(username = username,password = decode)
        obj.save()
        return HttpResponse('data save!!')
    template_name = 'adminlogin/register.html'
    return render(request,template_name)





def adminLoginView(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pwd')
        obj = AdminRegister.objects.get(username =u )
        encode =obj.password
        check = check_password(p,encode)
        if check is True:
            #print('correct password')
            return redirect('appointment')
        else:
            print('wrong passwords!!')
            return redirect('a_login')

    template_name = 'adminlogin/login.html'
    return render(request,template_name)

