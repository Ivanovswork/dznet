from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):

    users = models.ManyToManyField(User, verbose_name='Пользователи')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Сообщение')
    dt = models.DateTimeField(auto_now=True, verbose_name='Дата/время сообщения')
    text = models.TextField(blank=True, verbose_name='Текст сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
