from django.shortcuts import render
from django.views.generic import TemplateView


class MessageView(TemplateView):
    template_name = 'message/message.html'
