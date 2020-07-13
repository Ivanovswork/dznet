from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    dt = models.DateTimeField(auto_now=True, verbose_name='Дата/время сообщения')
    text = models.TextField(blank=True, verbose_name='Текст сообщения')

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='send_messages',
        verbose_name='Отправитель'
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='receive_messages',
        verbose_name='Получатель'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
