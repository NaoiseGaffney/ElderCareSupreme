from django.urls import path 
from .views import DashboardView, UserProfileCreate, UserProfileUpdate


urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('create_user_profile', UserProfileCreate.as_view(), name="user_profile_create"),
    path('update_user_profile/<int:pk>', UserProfileUpdate.as_view(), name="user_profile_update"),
]