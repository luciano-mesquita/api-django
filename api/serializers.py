from rest_framework import serializers
from .models import Cliente, Veiculo


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'idade']
    

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo']