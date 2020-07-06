from django.urls import path

from .views import CreateTaskView , ListMyTaskView, DeleteTaskView, SearchTaskView, UpdateTaskView, AssignAiderView


urlpatterns = [
    path('', ListMyTaskView.as_view(), name='task_list'),
    path('create_task', CreateTaskView.as_view(), name='create_task'),
    path('update_task/<int:pk>', UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('search_task', SearchTaskView.as_view(), name='search_task'),
    path('aider/<int:pk>', AssignAiderView.as_view(), name='aider'),
    path('api/post/<int:pk>/aider/', SearchTaskView.as_view(), name='aider_api'),
]