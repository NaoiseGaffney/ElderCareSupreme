from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserProfileForm
from .models import UserProfile


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Render dahsboard template
    """
    template_name = 'dashboard/dashboard.html'


class UserProfileCreate(LoginRequiredMixin, CreateView):
    """
    Create user profile after registration
    """
    template_name = 'dashboard/user_profile.html'
    form_class = UserProfileForm
    success_url = 'dashboard'

    def form_valid(self, form):
        print(self.request.user)
        instance = form.save(commit=False)
        instance.user_name = self.request.user
        instance.save()
        return redirect(self.get_success_url())


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    """
    Update View for user profile
    """
    template_name = 'dashboard/user_profile.html'
    form_class = UserProfileForm
    model = UserProfile
    success_url = 'dashboard'

    def get_queryset(self):
        """
        Make sure that user can acces only items that they own
        """
        queryset = super(UserProfileUpdate, self).get_queryset()
        queryset = queryset.filter(user_name=self.request.user)
        return queryset

    def form_valid(self, form):
        """
        Valid form
        """
        print(self.request.user)
        instance = form.save(commit=False)
        instance.user_name = self.request.user
        instance.save()
        return redirect(self.get_success_url())
