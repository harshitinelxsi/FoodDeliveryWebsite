from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import deliveryapp.models
from django.contrib.auth.hashers import make_password



def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def fail(request):
    return render(request, 'fail.html')
def successsignedup(request):
    return render(request, 'successsignedup.html')

def handelLogout(request):
    logout(request)
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        loginusername1 = request.POST['loginusername']
        loginpassword1 = request.POST['loginpassword']
        user = authenticate(username=loginusername1, password=loginpassword1)
        if user is not None:
            login(request, user)
            return render(request, 'success.html')

    return render(request, 'signin.html')



def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        print(email)
        password = request.POST['pswd']
        print(password)

        myuser = User.objects.create_user(username=email, password=password)
        myuser.save()
        login(request, myuser)
        return render(request, 'successsignedup.html')
    return render(request, 'signup.html')
