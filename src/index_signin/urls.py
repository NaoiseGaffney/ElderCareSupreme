from django.urls import path
from .views import IndexSignInView

urlpatterns = [
    path('', IndexSignInView.as_view(), name='index'),
]