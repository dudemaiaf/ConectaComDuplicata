from rest_framework import serializers
from .models import Teste

class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste
        fields = '__all__'