from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import random
from django.core.mail import send_mail
from django.conf import settings

def generate_verification_code():
    return str(random.randint(100000, 999999))


def send_verification_code_email(user_email,code):
    subject = 'Your Email Verification Code'
    message = f"Your verification code is: {code}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        try:
            new_user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],password=request.POST['password'])
            new_user.is_active = False
            new_user.save()
            verification_codes= {}
            code = generate_verification_code()
            verification_codes[new_user.email] = code
            send_verification_code_email(new_user.email, code)
            return render(request, "enter_code.html", {"email": new_user.email})
            
            
            
            messages.success(request,"user registered successfuly ","alert-success")
            return redirect('accounts:login_view')
    
        except Exception as e:
            messages.error(request,"user not registered, try again! ","alert-danger")
            print(e)
    return render(request,"accounts/signup.html")
def verfify_view(request):
    # to be continue .... 
    messages.success(request,"user registered successfuly ","alert-success")
    return redirect('accounts:login_view')
    return render(request,"accounts/signup.html")
    pass
def login_view(request:HttpRequest):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user :
            login(request,user)
            messages.success(request,f"welome {user.username}, you logged in successfuly","alert-success")
            return redirect('main:home_view')
        else:
            messages.success(request,"no such user , try again !","alert-danger")
    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"logged out successfuly ", "alert-warning")
    return redirect('accounts:login_view')
