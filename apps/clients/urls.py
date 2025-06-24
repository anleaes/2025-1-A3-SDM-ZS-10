from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'clients'

router = routers.DefaultRouter()
router.register('', views.ClientViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls))
]
