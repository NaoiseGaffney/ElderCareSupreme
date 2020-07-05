from django.contrib import admin

from .models import TaskCategory, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task_title', 'is_done', 'date_created')
    list_display_links = ('id', 'task_title')


class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('id', 'category')

 
admin.site.register(TaskCategory, TaskCategoryAdmin)
admin.site.register(Task, TaskAdmin)
