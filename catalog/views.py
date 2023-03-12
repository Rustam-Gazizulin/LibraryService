from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from catalog.models import Author, Books, Reader
from catalog.permissions import PermissionPolicyMixin, IsOwner
from catalog.serializers import AuthorViewSetSerializer, ReaderViewSetSerializer, BookViewSetSerializer


class AuthorViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorViewSetSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser]
    }


class ReaderViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderViewSetSerializer
    permission_classes_per_method = {
        'list': [IsAdminUser],
        'retrieve': [IsOwner | IsAdminUser],
        'create': [AllowAny],
        'update': [IsOwner | IsAdminUser],
        'destroy': [IsOwner | IsAdminUser]
    }


class BookViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookViewSetSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser]
    }


