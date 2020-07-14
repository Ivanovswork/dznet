from .views import index, UserViewSet
from django.urls import path
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('index/', index, name='index')
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns.extend(router.urls)
