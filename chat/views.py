from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer


def index(request):
    if request.user.is_authenticated:
        msg = 'Пользователь авторизован'
    else:
        msg = 'Пользователь неизвестен'

    context = {
        'msg': msg
    }
    return render(request, 'chat/index.html', context=context)


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()