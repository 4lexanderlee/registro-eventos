from rest_framework import generics
from .models import Evento
from .serializers import EventoSerializer

class EventoListCreateView(generics.ListCreateAPIView):
    """
    Lista todos los eventos o crea uno nuevo.
    """
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, actualiza o elimina un evento específico.
    """
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer