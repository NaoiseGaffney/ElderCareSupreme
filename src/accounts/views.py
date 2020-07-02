from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

# Create your views here.

class RegisterView(TemplateView):
    template_name = 'accounts/register.html'