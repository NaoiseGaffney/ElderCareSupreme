from django.urls import path

from .views import CreateTaskView 


urlpatterns = [
    # path('', ListTaskView.as_view(), 'create_task'),
    path('create_task', CreateTaskView.as_view(), 'create_task'),
    # path('update_task/<int:pk>', CreateTaskView.as_view(), 'update_task'),
    # path('delete_task/<int:pk>', CreateTaskView.as_view(), 'delete_task'),
]