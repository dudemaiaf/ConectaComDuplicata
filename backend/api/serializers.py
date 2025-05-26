from rest_framework import serializers
from . import models

class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teste
        fields = '__all__'

class ComunidadeSerializer(serializers.ModelSerializer):
    participando = serializers.SerializerMethodField()

    class Meta:
        model = models.Comunidade
        fields = ['id', 'titulo', 'descricao', 'participando']

    def get_participando(self, obj):
        request = self.context.get('request')
        user_id = request.query_params.get('user_id') if request else None
        if user_id:
            return obj.participantes.filter(id=user_id).exists()
        return False

class EventoSerializer(serializers.ModelSerializer):
    participando = serializers.SerializerMethodField()

    class Meta:
        model = models.Evento
        fields = ['id', 'titulo', 'descricao', 'diaHora', 'participando']

    def get_participando(self, obj):
        request = self.context.get('request')
        user_id = request.query_params.get('user_id') if request else None
        if user_id:
            return obj.participantes.filter(id=user_id).exists()
        return False

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Postagem
        fields = '__all__'
