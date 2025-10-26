from rest_framework import routers
from .views import CurriculumViewSet, StandardViewSet, LessonPlanViewSet

router = routers.DefaultRouter()
router.register(r'curriculums', CurriculumViewSet, basename='curriculum')
router.register(r'standards', StandardViewSet, basename='standard')
router.register(r'lessonplans', LessonPlanViewSet, basename='lessonplan')

urlpatterns = router.urls
