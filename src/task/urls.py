from django.urls import path

from .views import (CreateTaskView , ListMyTaskView, DeleteTaskView, 
                    SearchTaskView, UpdateTaskView, 
                    AssignAiderAPI, IsDoneAPI)


urlpatterns = [
    path('', ListMyTaskView.as_view(), name='task_list'),
    path('create_task', CreateTaskView.as_view(), name='create_task'),
    path('update_task/<int:pk>', UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('search_task', SearchTaskView.as_view(), name='search_task'),
    path('api/post/<int:pk>/aider/', AssignAiderAPI.as_view(), name='aider_api'),
    # path('is_done/<int:pk>', AssignAiderView.as_view(), name='is_done'),
    path('api/post/<int:pk>/is_done/', IsDoneAPI.as_view(), name='is_done_api'),
]