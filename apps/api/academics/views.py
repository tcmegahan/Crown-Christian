from rest_framework import viewsets
from .models import Curriculum, Standard, LessonPlan
from .serializers import CurriculumSerializer, StandardSerializer, LessonPlanSerializer
from apps.api.core.permissions import RolePermission


class CurriculumViewSet(viewsets.ModelViewSet):
 queryset = Curriculum.objects.all().order_by('name')
 serializer_class = CurriculumSerializer
 permission_classes = [RolePermission]
 required_permission = 'edit_curriculum'


class StandardViewSet(viewsets.ModelViewSet):
 queryset = Standard.objects.all()
 serializer_class = StandardSerializer
 permission_classes = [RolePermission]
 required_permission = 'edit_curriculum'


class LessonPlanViewSet(viewsets.ModelViewSet):
 queryset = LessonPlan.objects.all().order_by('-created_on')
 serializer_class = LessonPlanSerializer
 permission_classes = [RolePermission]
 required_permission = 'edit_curriculum'
