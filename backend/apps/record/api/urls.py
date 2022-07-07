from rest_framework import routers
from apps.record.api.views import *

router = routers.DefaultRouter()
router.register('resumes', ResumeViewSet, 'resumes')

urlpatterns = router.urls