from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at', 'updated_at', 'user')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'user__username')