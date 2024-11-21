from rest_framework import serializers
from .models import Announcement, Curia


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Announcement
        fields = [
            'curia',
            'date', 
            'title', 
            'body', 
            'image'
        ]


class CuriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Curia
        fields = [
            'name', 
            'iden', 
            'state', 
            'country', 
            'parish',
            'spiritual_director', 
            'creator', # Turn later into the logged in legionary and make read only
            'created_at',
            'managers', 
            'management_requests'
        ]
