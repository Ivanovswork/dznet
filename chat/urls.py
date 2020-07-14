from .views import index, UserViewSet, Login, Logout
from django.urls import path
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('index/', index, name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout')
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns.extend(router.urls)
