from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .froms import RegisterForm

# Create your views here.

class RegisterView(CreateView):
    """
    Register view template, render form.
    If  form valid, try to authenticate user and redirect to User Profile
    """
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 
                             f'Congratulations {username}! Your account has been created.')
            return redirect('user_profile_create')
        else:
            return redirect('index')
