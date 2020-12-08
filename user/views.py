from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.add_message(request,messages.SUCCESS,'Signed in.')
            return redirect('index')
        else:
            messages.add_message(request,messages.ERROR,'Account not found.')
            return redirect('login')
    else:
        return render(request,'user/login.html')

def register(request):
    if request.method == 'POST':       
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password==repassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.ERROR,'This username has been used before.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.add_message(request,messages.SUCCESS,'The account has been successfully created.')
                return redirect('login')
        else:
            messages.add_message(request,messages.ERROR,'Passwords do not match.')
            return redirect('register')
    else:
        return render(request,'user/register.html')
    

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,'You have been signed out.')
        return redirect('login')