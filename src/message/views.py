from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Message
from task.models import Task


class MessageView(LoginRequiredMixin, View):
    template_name = 'message/message.html'

    def get(self, request, *args, **kwargs):
        id_ = self.kwargs.get("pk")
        get_messages = Message.objects.filter(task=id_).order_by('date_created')
        user = self.request.user
        context = {
            'user': user,
            'get_messages': get_messages,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id_ = self.kwargs.get("pk")
        # Get task and slice to one, prevent error when None
        task = Task.objects.filter(id=id_)[:1]
        user = self.request.user
        message = self.request.POST.get('chat-message', None)
        if message is not None:
            Message.objects.create(user=user, task=task[0], message=message)
            # Increment by one message count
            if task:
                task[0].message_count += 1
                task[0].save()
        get_messages = Message.objects.filter(task=id_).order_by('date_created')
        context = {
            'user': user,
            'get_messages': get_messages,
        }
        return render(request, self.template_name, context)
