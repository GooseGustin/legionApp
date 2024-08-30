from rest_framework import routers 
from .views import FinancialRecordViewSet, FinancialSummaryViewSet

router = routers.DefaultRouter()
router.register('records', FinancialRecordViewSet)
router.register('summaries', FinancialSummaryViewSet)

urlpatterns = router.urls 