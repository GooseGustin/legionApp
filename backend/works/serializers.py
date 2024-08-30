from rest_framework import serializers 
from .models import *

class WorkSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Work
        fields = [
            'type', 
            'active', 
            'done', 
            'meeting',
            'details' 
        ]

class WorkListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = WorkList
        fields = [
            'praesidium',
            'details' 
        ]

class WorkSummarySerializer(serializers.ModelSerializer):
    class Meta: 
        model = WorkSummary
        fields = [
            'type', 
            'active', 
            'no_assigned',
            'no_done', 
            'report',
            'details' 
        ]

