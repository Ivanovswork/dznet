import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from chat.models import Message


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Команда для тестирования: она удаляет все сообщения из БД и заполняет её тестовыми сообщениями"""

        print('Начинаю работу...')

        # Удаляем все старые сообщения из базы
        Message.objects.all().delete()
        print('База очищена...')

        print('Добавляю сообщения в базу...')
        users = list(User.objects.all())
        for _ in range(len(users) * 50):
            sender = random.choice(users)
            receiver = random.choice(users)
            text = f'Пример текста для сообщения. ' \
                f'Текст должен быть достаточно длинным и включать случайный элемент: {random.randint(0, 1000000)}'
            Message.objects.create(
                text=text,
                sender=sender,
                receiver=receiver
            )

        print('Работа завершена...')
