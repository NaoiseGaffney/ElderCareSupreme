from django.urls import path

from .views import CreateTaskView , ListMyTaskView, DeleteTaskView, SearchTaskView, UpdateTaskView


urlpatterns = [
    path('', ListMyTaskView.as_view(), name='task_list'),
    path('create_task', CreateTaskView.as_view(), name='create_task'),
    path('update_task/<int:pk>', UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('search_task', SearchTaskView.as_view(), name='search_task'),
]