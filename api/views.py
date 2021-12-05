from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Veiculo
from .serializers import ClienteSerializer, VeiculoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
