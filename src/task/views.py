from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView


class CreateTaskView(CreateView):
    template_name = 'task/create_task.html'


# class UpdateTaskView
# class DeleteTaskView
# class ListTaskView