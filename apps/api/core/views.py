from rest_framework import viewsets, views, response, permissions
from .models import (
 Family,
 Guardian,
 Student,
 Term,
 Course,
 Section,
 Enrollment,
 Attendance,
 Grade,
 Ledger,
 LedgerLine,
 Communication,
)
from .serializers import (
 FamilySerializer,
 GuardianSerializer,
 StudentSerializer,
 TermSerializer,
 CourseSerializer,
 SectionSerializer,
 EnrollmentSerializer,
 AttendanceSerializer,
 GradeSerializer,
 LedgerSerializer,
 LedgerLineSerializer,
 CommunicationSerializer,
)

class FamilyViewSet(viewsets.ModelViewSet):
 queryset = Family.objects.all()
 serializer_class = FamilySerializer

class GuardianViewSet(viewsets.ModelViewSet):
 queryset = Guardian.objects.all()
 serializer_class = GuardianSerializer

class StudentViewSet(viewsets.ModelViewSet):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

class TermViewSet(viewsets.ModelViewSet):
 queryset = Term.objects.all()
 serializer_class = TermSerializer

class CourseViewSet(viewsets.ModelViewSet):
 queryset = Course.objects.all()
 serializer_class = CourseSerializer

class SectionViewSet(viewsets.ModelViewSet):
 queryset = Section.objects.all()
 serializer_class = SectionSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
 queryset = Enrollment.objects.all()
 serializer_class = EnrollmentSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
 queryset = Attendance.objects.all()
 serializer_class = AttendanceSerializer

class GradeViewSet(viewsets.ModelViewSet):
 queryset = Grade.objects.all()
 serializer_class = GradeSerializer

class LedgerViewSet(viewsets.ModelViewSet):
 queryset = Ledger.objects.all()
 serializer_class = LedgerSerializer

class LedgerLineViewSet(viewsets.ModelViewSet):
 queryset = LedgerLine.objects.all()
 serializer_class = LedgerLineSerializer

class CommunicationViewSet(viewsets.ModelViewSet):
 queryset = Communication.objects.all()
 serializer_class = CommunicationSerializer

class ProfileView(views.APIView):
 """Return minimal profile info: username, roles, and permission codes."""
 permission_classes = [permissions.AllowAny]

 def get(self, request):
 user = request.user if request.user and request.user.is_authenticated else None
 if not user:
 return response.Response({"authenticated": False, "roles": [], "permissions": []})

 profile = getattr(user, 'profile', None)
 roles = []
 perms = set()
 if profile:
 for role in profile.roles.all():
 roles.append(role.name)
 for p in role.permissions.all():
 perms.add(p.code)
 return response.Response({
 "authenticated": True,
 "username": user.username,
 "roles": roles,
 "permissions": sorted(list(perms)),
 })
