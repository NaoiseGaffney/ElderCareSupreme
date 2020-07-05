from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView


class HomePageView(TemplateView):
    """
    Render home/index page
    """
    template_name = "index.html"


class LogiInView(View):
    """
    Home page, with login box
    """
    template_view = "accounts/login.html"
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(request, f'Welcome back {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'The username or password is incorrect')
            return render(request, self.template_view, {})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_view, {})


class LogoutView(View):
    """
    Logout class
    """
    def get(self, request):
        logout(request)
        return redirect('index')
