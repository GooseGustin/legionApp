from rest_framework import authentication, permissions, viewsets
from .models import Legionary
from .serializers import LegionarySerializer

class LegionaryViewSet(viewsets.ModelViewSet): 
    queryset = Legionary.objects.all()
    serializer_class = LegionarySerializer
    # authentication_classes = [
    #     authentication.TokenAuthentication
    # ]
    permission_classes = [] # permissions.IsAuthenticated]


# Create user, delete user, edit details, edit praesidia managed
# edit curia managed, 