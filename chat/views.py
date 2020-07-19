from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .serializers import UserSerializer, MessageSerializer
from .models import Message


def get_token(user, refresh=False):
    _token = Token.objects.filter(user=user).first()
    if refresh or not _token:
        if _token:
            _token.delete()
        _token = Token.objects.create(user=user)
    return _token


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'chat/index.html', context={})

    user_list = list(User.objects.all())
    user_list.sort(key=lambda x: x.get_full_name() if x.get_full_name() else x.username)
    context = {
        'user_list': user_list,
    }
    return render(request, 'chat/index.html', context=context)


class Login(LoginView):
    template_name = 'chat/login.html'


class Logout(LogoutView):
    next_page = 'index'


# REST-Api


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def token(request):
    """Контроллер для получения токена по переданным учетным данным (логин/пароль)"""

    refresh = request.data.get('refresh', 'false')
    refresh = {'true': True, 'false': False}[refresh.lower()]

    _token = get_token(request.user, refresh)
    return Response({'token': _token.key})


class UserViewSet(ReadOnlyModelViewSet):
    """Контроллер для получения списка пользователей"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MessageView(ListCreateAPIView):
    """Контроллер для работы с сообщениями"""

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        """Пример параметров для запроса: ?sender=2&receiver=7&begin_id=229"""

        queryset = Message.objects.all()

        sender_id = self.request.query_params.get('sender')
        receiver_id = self.request.query_params.get('receiver')
        begin_id = self.request.query_params.get('begin_id')

        if sender_id:
            queryset = queryset.filter(sender_id=sender_id)
        if receiver_id:
            queryset = queryset.filter(receiver_id=receiver_id)
        if begin_id:
            queryset = queryset.filter(pk__gt=begin_id)

        return queryset

    def list(self, request, *args, **kwargs):
        # Блок диагностических сообщений
        # print('Пришел запрос в метод получения списка сообщений...')
        # print('is_ajax() ', request.is_ajax())
        # print('META:')
        # for k, v in request.META.items():
        #     print('  - ', k, ' = ', v)

        return super().list(request, *args, **kwargs)
