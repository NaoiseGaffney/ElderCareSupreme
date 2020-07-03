from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .froms import RegisterForm

# Create your views here.

class RegisterView(CreateView):
    """
    Register view template, display form and redirect to User Profile
    """
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('user_profile_create')
