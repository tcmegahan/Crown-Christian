from django.core.management.base import BaseCommand
from apps.api.core.models import Permission, Role, UserProfile, Family
from apps.api.academics.models import Curriculum, Standard, LessonPlan
from django.contrib.auth.models import User


class Command(BaseCommand):
 help = 'Seed default roles, permissions, sample curriculum and lesson plans'

 def handle(self, *args, **options):
 # Create permissions
 perms = [
 ('view_students', 'Can view students'),
 ('edit_students', 'Can edit students'),
 ('view_curriculum', 'Can view curriculum'),
 ('edit_curriculum', 'Can edit curriculum'),
 ]
 for code, desc in perms:
 Permission.objects.get_or_create(code=code, defaults={'description': desc})

 # Create roles
 roles = {
 'admin': ['view_students', 'edit_students', 'view_curriculum', 'edit_curriculum'],
 'teacher': ['view_students', 'view_curriculum', 'edit_curriculum'],
 'parent': ['view_students', 'view_curriculum'],
 'student': ['view_curriculum'],
 }
 for name, perm_codes in roles.items():
 role, _ = Role.objects.get_or_create(name=name, defaults={'description': f'{name} role'})
 for code in perm_codes:
 perm = Permission.objects.filter(code=code).first()
 if perm:
 role.permissions.add(perm)

 # Create sample curriculum and lesson
 cur, _ = Curriculum.objects.get_or_create(name='Bible Studies', defaults={'description': 'Sample Bible curriculum'})
 std, _ = Standard.objects.get_or_create(curriculum=cur, code='BS.1', defaults={'description': 'Understand Bible stories'})
 lp, _ = LessonPlan.objects.get_or_create(title='Creation Story', defaults={'curriculum': cur, 'objectives': 'Learn creation', 'activities': 'Read Genesis'})
 lp.standards.add(std)

 # Create admin user if not exists
 if not User.objects.filter(username='admin').exists():
 admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
 profile, _ = UserProfile.objects.get_or_create(user=admin)
 admin_role = Role.objects.filter(name='admin').first()
 if admin_role:
 profile.roles.add(admin_role)

 self.stdout.write(self.style.SUCCESS('Seed data created/ensured.'))
