from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'orders'

router = routers.DefaultRouter()
router.register('', views.OrderViewSet, basename='pedidos')

urlpatterns = [
    path('', include(router.urls))
]
