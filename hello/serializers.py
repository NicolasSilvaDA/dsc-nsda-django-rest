from rest_framework import serializers

class UsuarioSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    sobrenome = serializers.CharField(max_length=255)