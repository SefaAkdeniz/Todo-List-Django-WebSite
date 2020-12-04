from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.

def login(request):
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
                print('This username has been used before.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                print('The account has been successfully created.')
                return redirect('login')
        else:
            print('Passwords do not match.')
            return redirect('register')
    else:
        return render(request,'user/register.html')
    

def logout():
    pass