from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserProfileForm
from .models import UserProfile


class DashboardView(LoginRequiredMixin, View):
    """
    Render dahsboard template
    """
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        user_profile = UserProfile.objects.filter(user_name=user)
        context = {
            'user': user,
            'user_profile': user_profile,
        }
        return render(request, self.template_name, context)

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
        print(self.request.user)
        print(queryset)
        
        return queryset
    
    def get_object(self, **kwargs):
        id_ = self.kwargs.get('pk')
        profile = UserProfile.objects.filter(user_name = id_)
        if not profile:
            # Make sure to create a profile for user if not exists,
            # It happens with superusers and users created from admin panel
            UserProfile.objects.create(user_name = self.request.user)
        object = get_object_or_404(UserProfile, user_name = id_)
        return object

    def form_valid(self, form):
        """
        Valid form
        """
        print(self.request.user)
        instance = form.save(commit=False)
        instance.user_name = self.request.user
        instance.save()
        return redirect(self.get_success_url())
