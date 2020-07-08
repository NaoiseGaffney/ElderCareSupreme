from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'date_created')
    list_display_links = ('id', 'task', 'user')


admin.site.register(Message, MessageAdmin)
