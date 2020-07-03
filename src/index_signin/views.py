from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.generic import View

# Create your views here.
class IndexSignInView(View):
    template_view = "index.html"
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {username}!')
            return redirect('dashboard/dash.html')
        else:
            messages.error(request, 'The username or password is incorrect')
            return render(request, self.template_view, {})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_view, {})