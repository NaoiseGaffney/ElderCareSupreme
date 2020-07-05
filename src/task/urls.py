from django.urls import path

from .views import CreateTaskView , ListMyTaskView, DeleteTaskView


urlpatterns = [
    path('', ListMyTaskView.as_view(), name='task_list'),
    path('create_task', CreateTaskView.as_view(), name='create_task'),
    path('update_task/<int:pk>', CreateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
]