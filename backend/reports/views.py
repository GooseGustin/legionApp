# from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import * 
from .models import (
    Report, FunctionAttendance, MembershipDetails, Achievement
)

# Create your views here.
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all() # filter by manager
    serializer_class = ReportSerializer

class FunctionAttendanceViewSet(viewsets.ModelViewSet):
    queryset = FunctionAttendance.objects.all()
    serializer_class = FunctionAttendanceSerializer

class MembershipDetailsViewSet(viewsets.ModelViewSet):
    queryset = MembershipDetails.objects.all()
    serializer_class = MembershipDetailsSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializers