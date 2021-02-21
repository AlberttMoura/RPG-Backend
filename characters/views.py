from rest_framework import viewsets
from .models import NPC
from .serializers import NPCSerializer

class NPCViewSet(viewsets.ModelViewSet):
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer

