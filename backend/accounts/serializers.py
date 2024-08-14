from rest_framework import serializers
from .models import Legionary

class LegionarySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Legionary        
        fields = [
            'user', 
            'status', 
            'curia_managed', 
            'is_manager'
        ]