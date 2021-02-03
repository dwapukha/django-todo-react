from django.contrib import admin
from .models import todo

# Register your models here.
@admin.register(todo)
class todoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    list_filter = ('completed',)
    search_fields = ('title',)