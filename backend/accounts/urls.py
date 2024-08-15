from rest_framework import routers 
from .views import LegionaryViewSet

router = routers.DefaultRouter()
router.register('legionaries', LegionaryViewSet)

urlpatterns = router.urls 