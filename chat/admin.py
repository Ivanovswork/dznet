from django.contrib import admin
from .models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['users_list']

    def users_list(self, rec):
        return '/'.join([user.username for user in rec.users.all()])

    users_list.short_description = 'Пользователи в чате'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['chat', 'dt', 'text']
