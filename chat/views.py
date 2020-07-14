from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .serializers import UserSerializer


def index(request):
    return render(request, 'chat/index.html', context={})


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class Login(LoginView):
    template_name = 'chat/login.html'


class Logout(LogoutView):
    next_page = 'index'
