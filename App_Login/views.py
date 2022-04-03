from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from App_Login.forms import CreateNewUser

from django.contrib.auth import authenticate, login, logout

from App_Login.models import UserProfile

def sign_up(request):
    form = CreateNewUser()
    registered = False

    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            pass
    return render(request, 'App_Login/signup.html', context={'title': 'Signup page', 'form': form})
