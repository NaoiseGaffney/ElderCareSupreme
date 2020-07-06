from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, View
from django.db.models import Q
from django.contrib import messages

from .forms import TaskForm
from .models import Task
from dashboard.models import UserProfile


class ListMyTaskView(LoginRequiredMixin, ListView):
    template_name = 'task/my_tasks.html'
    model = Task
    paginate_by = 5
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super(ListMyTaskView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user).order_by('-date_created')
        return queryset


class CreateTaskView(LoginRequiredMixin ,CreateView):
    template_name = 'task/create_task.html'
    form_class = TaskForm
    success_url = 'task_list'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        messages.success(self.request, 
                             f'Your task is created!')
        return redirect(self.success_url)


class DeleteTaskView(LoginRequiredMixin, View):
    """
    Delte view, check if user is owner of that post
    """
    template_name = 'task/task_removed.html'

    def get(self, request, *args, **kwargs):
        id_ = self.kwargs['pk']
        task = Task.objects.filter(id=id_, user=self.request.user).delete()
        print(task)
        return render(request, self.template_name, {})


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = 'task/update_task.html'
    form_class = TaskForm
    model = Task
    success_url = 'task_list'

    def get_queryset(self):
        queryset = super(UpdateTaskView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get('pk')
        object = get_object_or_404(Task, pk=id_)
        print(object)
        return object

    def form_valid(self, form):
        """
        Valid form
        """
        print(self.request.user)
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        messages.success(self.request, 
                             f'Your task was updated!')
        return redirect(self.get_success_url())


class SearchTaskView(LoginRequiredMixin, View):
    template_name = 'task/search_task.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        user = self.request.user
        # check if user is an aider
        is_aider = UserProfile.objects.filter(user_name=user, is_aider=True)
        if is_aider:
            tasks = Task.objects.filter(is_done=False)
            context = {
                'tasks': tasks,
            }
            return render(request, self.template_name, context)
        else:
            return redirect('task_list')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
