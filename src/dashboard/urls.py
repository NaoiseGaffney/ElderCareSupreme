from django.urls import path 
from .views import DashboardView, UserProfileUpdate


urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('update_user_profile/<int:pk>', UserProfileUpdate.as_view(), name="user_profile_update"),
]