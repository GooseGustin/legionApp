from rest_framework import serializers
from .models import Legionary

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

class LegionarySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta: 
        model = Legionary        
        fields = [
            'user', 
            'status', 
            'curia_managed', 
        ]