from django.db import models
import uuid


class Curriculum(models.Model):
 curriculum_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
 name = models.CharField(max_length=255)
 description = models.TextField(blank=True)

 class Meta:
 db_table = 'academics_curriculum'

 def __str__(self):
 return self.name


class Standard(models.Model):
 standard_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
 curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, related_name='standards')
 code = models.CharField(max_length=100)
 description = models.TextField(blank=True)

 class Meta:
 db_table = 'academics_standard'

 def __str__(self):
 return f"{self.curriculum.name} - {self.code}"


class LessonPlan(models.Model):
 lesson_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
 title = models.CharField(max_length=255)
 curriculum = models.ForeignKey(Curriculum, on_delete=models.SET_NULL, null=True, blank=True)
 standards = models.ManyToManyField(Standard, blank=True)
 objectives = models.TextField(blank=True)
 activities = models.TextField(blank=True)
 created_on = models.DateTimeField(auto_now_add=True)

 class Meta:
 db_table = 'academics_lessonplan'

 def __str__(self):
 return self.title
