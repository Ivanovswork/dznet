from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .serializers import UserSerializer


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

    # Тестовый код для генерирования сообщений
    import random
    from datetime import datetime
    message_list = []
    for _ in range(50):
        message_list.append(
            {
                'dt': datetime.now(),
                'text': 'Тестовое сообщение для проверки отображения сообщений. В том числе с длинным текстом',
                'sender': random.choice(user_list)
            }
        )

    context = {
        'user_list': user_list,
        'message_list': message_list
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
