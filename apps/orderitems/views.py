from django.shortcuts import render

from rest_framework import viewsets
from .models import Orderitem
from .serializer import OrderitemSerializer

class OrderitemViewSet(viewsets.ModelViewSet):
    queryset = Orderitem.objects.all()
    serializer_class = OrderitemSerializer
