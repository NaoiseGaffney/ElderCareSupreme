from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, TemplateView

from .forms import TaskForm
from .models import Task


class ListMyTaskView(LoginRequiredMixin, ListView):
    template_name = 'task/my_tasks.html'
    model = Task
    paginate_by = 5
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super(ListMyTaskView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CreateTaskView(LoginRequiredMixin ,CreateView):
    template_name = 'task/create_task.html'
    form_class = TaskForm
    success_url = 'task_list'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect(self.success_url)


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = 'task_list'

    def get_queryset(self):
        queryset = super(DeleteView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
# class UpdateTaskView

