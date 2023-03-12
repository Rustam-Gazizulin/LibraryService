from rest_framework.permissions import BasePermission

from catalog.models import Reader


class PermissionPolicyMixin:
    def check_permissions(self, request):
        try:
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if handler and self.permission_classes_per_method and self.permission_classes_per_method.get(handler.__name__):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class IsOwner(BasePermission):
    message = 'Недостаточно полномочий для данного запроса'

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.pk:
            return True
        return False


