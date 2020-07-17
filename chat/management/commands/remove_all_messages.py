from django.core.management.base import BaseCommand
from chat.models import Message


class Command(BaseCommand):

    def handle(self, *args, **options):
        Message.objects.all()
        print('Все сообщения удалены...')
