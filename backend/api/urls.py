from django.urls import include, path 
from rest_framework.authtoken.views import obtain_auth_token
# from . import views 

urlpatterns = [
    path('auth/', obtain_auth_token), 
    path('api-auth/', include("rest_framework.urls")), # For logging in
    # path('', views.api_home), # localhost:api/
    path('', include('accounts.urls')),
    path('', include('curia.urls')),
    path('', include('meetings.urls')),
    path('', include('works.urls')),
    path('', include('reports.urls')),
    path('', include('praesidium.urls')),
    path('', include('finance.urls')),
]