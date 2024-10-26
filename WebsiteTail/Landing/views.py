from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from WebsiteTail.forms import SignupForm, LoginForm, CustomSetPasswordForm
from django.views import View
from json import dumps
from . import models



def index(request):
    #template = loader.get_template("html.html")
    # return render(request, "aff/../templates/html.html")
    #print(currUser.favorites)
    return render(request, "home.html")

    #return HttpResponse(template.render({}, request))
    #return HttpResponse("Are you hungry Atlanta?")

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('index')


def user_resetpassword(request):
   if request.method == "POST":
       fm = CustomSetPasswordForm(user=request.user, data=request.POST)
       if fm.is_valid():
           fm.save()
           # Update user session
           update_session_auth_hash(request, fm.user)
           return redirect('login')
   else:
       fm = CustomSetPasswordForm(user=request.user)


   return render(request, 'reset.html', {'form': fm})


def about(request):
    template_name = "aff/about.html"
    return render(request, "aff/../../templates/about.html")

def builder(request):
    template_name = "aff/notfound.html"
    return render(request, "aff/../../templates/notfound.html")



def explore(request):
    # template_name = "aff/explore.html"
    # return render(request, "aff/../../templates/explore.html")
    return redirect('map_view')
