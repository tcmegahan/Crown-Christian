from rest_framework import viewsets
from .models import Curriculum, Standard, LessonPlan
from .serializers import CurriculumSerializer, StandardSerializer, LessonPlanSerializer


class CurriculumViewSet(viewsets.ModelViewSet):
 queryset = Curriculum.objects.all().order_by('name')
 serializer_class = CurriculumSerializer


class StandardViewSet(viewsets.ModelViewSet):
 queryset = Standard.objects.all()
 serializer_class = StandardSerializer


class LessonPlanViewSet(viewsets.ModelViewSet):
 queryset = LessonPlan.objects.all().order_by('-created_on')
 serializer_class = LessonPlanSerializer
