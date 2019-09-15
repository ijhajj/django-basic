from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_name = request.POST['user_name']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'User already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'User with this email already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/travello')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        user_name = request.POST['user_name']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:    #that is if user exists
            auth.login(request, user)
            return redirect('/travello')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/travello')
