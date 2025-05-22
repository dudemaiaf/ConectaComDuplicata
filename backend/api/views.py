from rest_framework import viewsets
from .models import Teste
from .serializers import TesteSerializer

class TesteViewSet(viewsets.ModelViewSet):
    queryset = Teste.objects.all()
    serializer_class = TesteSerializer