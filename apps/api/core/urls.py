from django.urls import path, include
from rest_framework import routers
from .views import (
 FamilyViewSet,
 GuardianViewSet,
 StudentViewSet,
 TermViewSet,
 CourseViewSet,
 SectionViewSet,
 EnrollmentViewSet,
 AttendanceViewSet,
 GradeViewSet,
 LedgerViewSet,
 LedgerLineViewSet,
 CommunicationViewSet,
 ProfileView,
)

router = routers.DefaultRouter()
router.register(r'families', FamilyViewSet, basename='family')
router.register(r'guardians', GuardianViewSet, basename='guardian')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'terms', TermViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'ledgers', LedgerViewSet)
router.register(r'ledger-lines', LedgerLineViewSet)
router.register(r'communications', CommunicationViewSet, basename='communication')

urlpatterns = [
 path('', include(router.urls)),
 # profile endpoint
 path('profile/', ProfileView.as_view(), name='profile'),
]
