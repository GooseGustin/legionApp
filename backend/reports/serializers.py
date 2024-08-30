from rest_framework import serializers 
from .models import * 

class ReportSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Report 
        fields = [
            'praesidium', 'submission_date', 'last_submission_date', 
            'report_number', 'report_period', 'last_curia_visit_date', 
            'last_curia_visitors', 'officer_curia_attendance', 
            'officer_meeting_attendance', 'extension_plans', 
            'problems', 'remarks', 'no_meetings_expected', 
            'no_meetings_held', 'avg_attendance', 'poor_attendance_reason'
        ]

class FunctionAttendanceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FunctionAttendance
        fields = [
            'report', 'name', 'date', 'current_year_attendance', 
            'previous_year_attendance'
        ]

class MembershipDetailsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MembershipDetails
        fields = [
            'report', 'senior_praesidia', 'junior_praesidia', 
            'active_members', 'probationary_members', 
            'auxiliary_members', 'adjutorian_members',
            'praetorian_members'
        ]

class AchievementSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Achievement
        fields = [
            'report', 'no_recruited', 'no_baptized', 'no_confirmed', 
            'no_first_communicants', 'others'
        ]
