from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from curia.models import Announcement, Curia
from finance.models import (AcctAnnouncement, AcctStatement, Expenses, FinancialRecord, FinancialSummary)
from meetings.models import Meeting
from praesidium.models import Praesidium, Reminder
from reports.models import (Achievement, FunctionAttendance, MembershipDetails, Report)
from works.models import Work, WorkList, WorkSummary

# Create Groups
legionary_group, created = Group.objects.get_or_create(name='Legionary')
manager_group, created = Group.objects.get_or_create(name='Manager')
staff_group, created = Group.objects.get_or_create(name='Staff')
admin_group, created = Group.objects.get_or_create(name='Admin')

# Define content types for all models
models = [Curia, Announcement, Praesidium, Reminder, Meeting, 
          Work, WorkSummary, WorkList, FinancialSummary, FinancialRecord,
          AcctAnnouncement, AcctStatement, Expenses, Report, 
          FunctionAttendance, MembershipDetails, Achievement]

permissions = {
    'Legionary': {
        'curia': ['add', 'view'],
        'praesidium': ['add', 'view'],
        'default': ['view']
    },
    'Manager': {
        'default': ['add', 'view', 'change', 'delete']
    },
    'Staff': {
        'curia': ['view'],
        'praesidium': ['view'],
        'announcement': ['view', 'delete'],
        'default': []
    }
}

# Assign Permissions
for model in models:
    content_type = ContentType.objects.get_for_model(model)
    model_name = model.__name__.lower()
    
    for group_name, perms in permissions.items():
        group = Group.objects.get(name=group_name)
        model_perms = perms.get(model_name, perms.get('default', []))
        
        for perm in model_perms:
            permission = Permission.objects.get(codename=f'{perm}_{model_name}', content_type=content_type)
            group.permissions.add(permission)

# Admin Group should have all permissions
admin_group.permissions.set(Permission.objects.all())
