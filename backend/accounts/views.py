from rest_framework import viewsets 
from .models import Legionary
from .serializers import LegionarySerializer


class LegionaryViewSet(viewsets.ModelViewSet): 
    queryset = Legionary.objects.all()
    serializer_class = LegionarySerializer


# Create user, delete user, edit details, edit praesidia managed
# edit curia managed, 