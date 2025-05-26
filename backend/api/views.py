from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, date, timedelta
from . import models
from . import serializers

class TesteViewSet(viewsets.ModelViewSet):
    queryset = models.Teste.objects.all()
    serializer_class = serializers.TesteSerializer

class ComunidadeView(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ComunidadeSerializer
    queryset = models.Comunidade.objects.filter(ativo=True)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Comunidade desativada"}, status=status.HTTP_204_NO_CONTENT)
    
class EventoView(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.EventoSerializer
    queryset = models.Evento.objects.filter(ativo=True)
    # def get_queryset(self):

    #     return queryset
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Evento desativado"}, status=status.HTTP_204_NO_CONTENT)

class PostagemView(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PostagemSerializer
    # queryset = models.Evento.objects.filter(ativo=True)
    def get_queryset(self):
        # p_usuario = self.request.query_params.get('servidor', None)
        p_comunidade = self.request.query_params.get('comunidade', None)
        if (p_comunidade):
            queryset = models.Postagem.objects.filter(comunidade=p_comunidade, ativo=True)
        else:
            queryset = models.Postagem.objects.filter(ativo=True)
        return queryset
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Postagem desativado"}, status=status.HTTP_204_NO_CONTENT)