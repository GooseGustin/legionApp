from django.shortcuts import render
from rest_framework import viewsets
from .models import Announcement, Curia
from .serializers import AnnouncementSerializer, CuriaSerializer
# Create your views here.
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class CuriaViewSet(viewsets.ModelViewSet):
    queryset = Curia.objects.all()
    serializer_class = CuriaSerializer