# from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import * 

# Create your views here.
class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer

class FinancialSummaryViewSet(viewsets.ModelViewSet):
    queryset = FinancialSummary.objects.all()
    serializer_class = FinancialSummarySerializer