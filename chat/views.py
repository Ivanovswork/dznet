from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        msg = 'Пользователь авторизован'
    else:
        msg = 'Пользователь неизвестен'

    context = {
        'msg': msg
    }
    return render(request, 'chat/index.html', context=context)
