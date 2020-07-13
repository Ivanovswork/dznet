from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['dt', 'text', 'sender', 'receiver']
    list_display_links = ['text']
