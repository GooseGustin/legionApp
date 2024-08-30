from rest_framework import serializers
from .models import * 

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Expenses
        fields = [
            'extension', 'remittance', 
            'stationery', 'altar', 
            'bouquet', 'others'
        ]

class AcctStatementSerializer(serializers.ModelSerializer):
    expenses = ExpensesSerializer()
    class Meta: 
        model = AcctStatement
        fields = [
            'acf', 'sbc', 'balance', 'expenses'
        ]

class AcctAnnouncementSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AcctAnnouncement
        fields = [
            'sbc', 'collection_1', 'collection_2'
        ]

class FinancialRecordSerializer(serializers.ModelSerializer):
    acct_statement = AcctStatementSerializer()
    acct_announcement = AcctAnnouncementSerializer()
    class Meta: 
        model = FinancialRecord
        fields = [
            'meeting', 'acct_statement', 'acct_announcement'
        ]


class FinancialSummarySerializer(serializers.ModelSerializer):
    class Meta: 
        model = FinancialSummary
        fields = [
            'report', 'abf', 'sbc', 'expenses', 
            'report_production'
        ]

