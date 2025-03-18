from django.shortcuts import render,redirect
from django.http import HttpRequest
# Create your views here.

def home_view(request):
    return render(request,'main/home.html')

def theme_mode_view(request:HttpRequest):
    referer = request.META.get('HTTP_REFERER', '/')
    response = redirect(referer)
    current_mode = request.COOKIES.get('dark_mode')
    
    if current_mode == 'true':
        response.set_cookie('dark_mode', 'false')
    else:
        response.set_cookie('dark_mode', 'true')
    return response