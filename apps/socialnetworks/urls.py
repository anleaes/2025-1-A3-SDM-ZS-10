from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'socialnetworks'

router = routers.DefaultRouter()
router.register('', views.SocialnetworkViewSet, basename='redessociais')

urlpatterns = [
    path('', include(router.urls))
]
