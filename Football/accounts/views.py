from django.shortcuts import render
from django.contrib.auth.models import User 
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        new_user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'])
        new_user.save()
    return render(request,"accounts/signup.html")
