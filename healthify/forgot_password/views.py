from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import logout
# Create your views here.
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('uname')

        if not email or not username:
            messages.error(request,'both fields are required!')
            return redirect('resetpass')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Username Does not Exist!')
            return redirect('resetpass')
        user1 = User.objects.get(username=username)
        user= user1.id
        if not User.objects.filter(email = email).exists():
            messages.error(request,'Email Id Does not Exist!')
            return redirect('resetpass')
        else:
            send_mail (
                'Forgot password link',
                f'hey {username}''\n'
                'click on the link to reset password''\n'
                f'http://127.0.0.1:8000/forgot_pass/reset/''\n',
                'rahulvethekar95@gmail.com',
                [user1.email],
                fail_silently = False,

            )
            messages.success(request,'Email has been send successfully on your email id, please check it.')
            return redirect('resetpass')


    template_name = 'forgot_password/forgot.html'
    return render(request,template_name)

def changepassword(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        oldpwd = request.POST.get('oldpwd')
        newpwd1 = request.POST.get('newpwd1')
        newpwd2 = request.POST.get('newpwd2')




        if not User.objects.filter(username= uname).exists():
            messages.error(request,'Username does not exist!')
            return redirect('changepassword')

        user = User.objects.get(username=uname)
        encoded = user.password
        check = check_password(oldpwd, encoded)
        if check is False:
            messages.error(request,'Wrong old password!')

        if  newpwd1 != newpwd2:
            messages.error(request,'password1 and password2 does not match!')
            return redirect('changepassword')
        encodedpass = make_password(newpwd1)
        user.password = encodedpass
        user.save()
        messages.success(request,'You have successfully changed your password!')
        return redirect('changepassword')
    template_name = 'forgot_password/changepassword.html'
    return render(request,template_name)




def forgotDetailsView(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        # oldpwd = request.POST.get('oldpwd')
        newpwd1 = request.POST.get('newpwd1')
        newpwd2 = request.POST.get('newpwd2')

        if not User.objects.filter(username=uname).exists():
            messages.error(request, 'Username does not exist!')
            return redirect('resetpassword')

        if newpwd1 != newpwd2:
            messages.error(request, 'password1 and password2 does not match!')
            return redirect('resetpassword')
        user = User.objects.get(username=uname)

        encodedpass = make_password(newpwd1)
        user.password = encodedpass
        user.save()
        messages.success(request, 'You have successfully changed your password!')
        return redirect('resetpassword')
    template_name = 'forgot_password/forgotdetails.html'
    return render(request, template_name)











