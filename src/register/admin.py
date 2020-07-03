from django.contrib import admin
from .models import UserRole, UserProfile

# Register your models here.
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')
    list_display_links = ('id', 'role')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'post_code', 'role', 'city')
    list_display_links = ('id', 'user_name')

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(UserProfile, UserProfileAdmin)