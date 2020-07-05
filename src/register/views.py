from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .froms import RegisterForm
from dashboard.models import UserProfile

# Create your views here.

class RegisterView(CreateView):
    """
    Register view template, render form.
    If  form valid, try to authenticate user and redirect to User Profile
    """
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        # override post method, first logout user then pass form
        logout(self.request)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            # Login user, create user profile and redirect to update profile page
            login(self.request, user)
            user_profile = UserProfile.objects.create(user_name=user)
            user_profile.save()
            print(user_profile)
            messages.success(self.request, 
                             f'Congratulations {username}! Your account has been created.')
            return redirect('update_user_profile', pk=user.id)
            # return HttpResponseRedirect('/dashboard/user_profile_update/'+ user_profile.id)
        else:
            return redirect('index')
