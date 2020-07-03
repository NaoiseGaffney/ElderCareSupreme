from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class IndexSignInView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard/dash.html')
        else:
            