from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'post_code', 'is_aider', 'city')
    list_display_links = ('id', 'user_name')


admin.site.register(UserProfile, UserProfileAdmin)