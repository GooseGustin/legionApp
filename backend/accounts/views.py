from rest_framework import authentication, generics, permissions, viewsets
from .models import Legionary
from .serializers import LegionarySerializer

class LegionaryViewSet(viewsets.ModelViewSet): 
    queryset = Legionary.objects.all()
    serializer_class = LegionarySerializer
    authentication_classes = [
    #     authentication.TokenAuthentication
        authentication.SessionAuthentication
    ]
    permission_classes = [permissions.DjangoModelPermissions] 
    # IsAuthenticated] # AllowAny] # permissions.IsAuthenticated]
