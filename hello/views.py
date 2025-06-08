# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer

# Create your views here.


@api_view(['GET'])
def hello_world(request):
    return Response("Hello World!")

@api_view(['GET'])
def hello_world_param(request):
    nome = request.query_params.get('nome')
    sobrenome = request.query_params.get('sobrenome')

    return Response(f'Hello, {nome} {sobrenome}!!')

@api_view(['GET'])
def hello_world_path(request, nome, sobrenome):
    return Response(f'Hello. {nome} {sobrenome}!!')

@api_view(['GET'])
def hello_world_path_valor(request, nome, sobrenome, valor):
    return Response(f'Hello, {nome} {sobrenome}!! - Valor: {valor}')

@api_view(['POST'])
def hello_world_usuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        nome = serializer.validated_data['nome'] # Tratar depois
        sobrenome = serializer.validated_data['sobrenome'] # Tratar depois
        return Response(f'Hello, {nome} {sobrenome}!!')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def hello_world_json(request):
    return Response(f'Hello, {request.data}!!')