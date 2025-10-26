from rest_framework import serializers
from .models import Curriculum, Standard, LessonPlan


class StandardSerializer(serializers.ModelSerializer):
 class Meta:
 model = Standard
 fields = ('standard_id', 'code', 'description')


class CurriculumSerializer(serializers.ModelSerializer):
 standards = StandardSerializer(many=True, read_only=True)

 class Meta:
 model = Curriculum
 fields = ('curriculum_id', 'name', 'description', 'standards')


class LessonPlanSerializer(serializers.ModelSerializer):
 curriculum = CurriculumSerializer(read_only=True)
 curriculum_id = serializers.UUIDField(write_only=True, required=False, allow_null=True)

 class Meta:
 model = LessonPlan
 fields = ('lesson_id', 'title', 'curriculum', 'curriculum_id', 'objectives', 'activities', 'created_on')
