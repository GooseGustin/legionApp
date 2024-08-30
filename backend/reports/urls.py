from rest_framework import routers 
from .views import * 

router = routers.DefaultRouter()
router.register('report', ReportViewSet)
router.register('function', FunctionAttendanceViewSet)
router.register('membership', MembershipDetailsViewSet)
router.register('achievement', AchievementViewSet)

urlpatterns = router.urls 