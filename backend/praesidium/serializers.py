from rest_framework import serializers 
from .models import Praesidium, Reminder

class PraesidiumSerializer(serializers.ModelSerializer):
    # remove iden from serializer
    class Meta: 
        model = Praesidium 
        fields = [
            'name', 'state', 'country', 'parish', 'curia', 
            'iden', 'address', 'meeting_time', 'inaug_date', 
            'president', 'pres_app_date', 'vice_president', 
            'vp_app_date', 'secretary', 'sec_app_date', 
            'treasurer', 'tres_app_date', 'managers', 'members',
            'membership_requests', 'next_report_deadline', 
            'created_at'
        ]

# praesidium serializer for staff 

class ReminderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reminder 
        fields = [
            'praesidium', 
            'content', 
            'deadline'
        ]