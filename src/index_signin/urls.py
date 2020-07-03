from django.urls import path
from .views import IndexSignInView, LogoutView

urlpatterns = [
    path('', IndexSignInView.as_view(), name='index'),
    path('/userlogout', LogoutView.as_view(), name='logout'),
]