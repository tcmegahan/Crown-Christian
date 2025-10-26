from rest_framework import permissions


class RolePermission(permissions.BasePermission):
 """Custom permission that checks user profile roles & permissions.

 Views can set `required_permission` attribute (string) to indicate the
 permission code required for non-safe methods (POST/PUT/PATCH/DELETE).
 If not set, default is to allow authenticated users to write.
 """

 def has_permission(self, request, view):
 # Safe methods are allowed for everyone (depending on global setting)
 if request.method in permissions.SAFE_METHODS:
 return True

 # For non-safe methods, require authentication
 if not request.user or not request.user.is_authenticated:
 return False

 required = getattr(view, 'required_permission', None)
 # If no specific permission configured, allow authenticated users
 if not required:
 return True

 # Check user's profile for permissions
 profile = getattr(request.user, 'profile', None)
 if not profile:
 return False

 # gather permission codes
 perms = set()
 for role in profile.roles.all():
 for p in role.permissions.all():
 perms.add(p.code)

 return required in perms
