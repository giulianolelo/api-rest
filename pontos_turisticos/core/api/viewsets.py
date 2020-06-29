from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializer import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
   
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]