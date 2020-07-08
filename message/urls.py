from django.urls import path
from .views import MessageView


urlpatterns = [
    path('<int:pk>', MessageView.as_view(), name="message"),
]
