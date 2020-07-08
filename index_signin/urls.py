from django.urls import path
from .views import LogiInView, LogoutView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('login', LogiInView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]