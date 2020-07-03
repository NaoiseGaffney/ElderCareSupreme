from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .froms import RegisterForm

# Create your views here.

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')