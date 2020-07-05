from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
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
    template_name = 'task/task_removed.html'

    def get_queryset(self):
        queryset = super(DeleteView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_object(self, *args, **kwargs):
        tasks = get_object_or_404(Task, pk=self.kwargs['pk'])
        return tasks


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/update_task.html'
    form_class = TaskForm
    model = Task
    success_url = 'task_list'

    def get_queryset(self):
        queryset = super(DeleteView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_object(self, *args, **kwargs):
        tasks = get_object_or_404(Task, pk=self.kwargs['pk'])
        return tasks